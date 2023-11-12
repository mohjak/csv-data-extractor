import pandas as pd
import os
import sys


def process_csv_files(source):
    total_source_records = 0
    total_output_records = 0

    if os.path.isdir(source):
        # Process all files in the directory
        output_dir = os.path.join(source, 'out')
        ensure_directory(output_dir)
        for filename in os.listdir(source):
            if filename.endswith('.csv'):
                file_path = os.path.join(source, filename)
                source_count, output_count = process_file(
                    file_path, output_dir)
                total_source_records += source_count
                total_output_records += output_count
    elif os.path.isfile(source) and source.endswith('.csv'):
        # Process a single file
        output_dir = os.path.join(os.path.dirname(source), 'out')
        ensure_directory(output_dir)
        total_source_records, total_output_records = process_file(
            source, output_dir)
    else:
        print(
            f"The path provided is neither a CSV file nor a directory: {source}")

    print(f"Total records in source files: {total_source_records}")
    print(f"Total records in output files: {total_output_records}")


def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def process_file(file_path, output_dir):
    source_record_count = 0
    output_record_count = 0

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        source_record_count = len(df)

        # Check if the required columns exist
        required_columns = ['وسوم داخلية', 'Slug', 'Title',
                            'Content', 'سؤال الفتوى', 'جواب الفتوى']
        if not all(column in df.columns for column in required_columns):
            print(
                f"Required columns {required_columns} not found in {file_path}. Skipping file.")
            return source_record_count, output_record_count

        # Convert columns to string to ensure .str methods work
        df[required_columns] = df[required_columns].astype(str)

        # Filter records
        filtered_df = df[df['وسوم داخلية'].str.contains(
            'تهجير البيانات', na=False)]
        output_record_count = len(filtered_df)

        # Sort based on the character count
        filtered_df = filtered_df.assign(
            سؤال_len=filtered_df['سؤال الفتوى'].str.len(),
            جواب_len=filtered_df['جواب الفتوى'].str.len()
        ).sort_values(by=['سؤال_len', 'جواب_len'])

        # Add 'Old CMS Edit URL' column
        filtered_df['Old CMS Edit URL'] = 'https://sh-albarrak.com/admin/posts/fatawa/' + \
            filtered_df['Slug'] + '/update'

        # Add 'Old Website URL' column
        filtered_df['Old Website URL'] = 'https://sh-albarrak.com/article/' + \
            filtered_df['Slug']

        # Select only the required columns for output
        output_columns = ['Title', 'Content', 'وسوم داخلية', 'Slug',
                          'سؤال الفتوى', 'جواب الفتوى', 'Old CMS Edit URL', 'Old Website URL']
        filtered_df = filtered_df[output_columns]

        # Write to CSV in the 'out' folder, maintaining original file name
        output_file_path = os.path.join(
            output_dir, os.path.basename(file_path))
        filtered_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

    except KeyError as e:
        print(f"KeyError in file {file_path}: {e}. Skipping file.")

    return source_record_count, output_record_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_or_directory_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    process_csv_files(source_path)

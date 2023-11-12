import unittest
import os
import pandas as pd
from csv_data_extractor.extractor import process_csv_files


class TestProcessCSVFiles(unittest.TestCase):

    def setUp(self):
        self.input_dir = 'tests/data/'
        self.sample_input_file = os.path.join(
            self.input_dir, 'sample_data.csv')
        # The output file will be in the same directory as the input file, but within an 'out' subdirectory
        self.expected_output_file = os.path.join(
            self.input_dir, 'out', 'sample_data.csv')

    def test_process_csv_files(self):
        # Ensure the 'out' directory exists
        os.makedirs(os.path.dirname(self.expected_output_file), exist_ok=True)

        # Run the process_csv_files function on the sample data
        process_csv_files(self.sample_input_file)

        # Check if the output file is created
        self.assertTrue(os.path.isfile(self.expected_output_file))

        # You can include additional checks here if needed, like verifying the content of the output file
        # output_df = pd.read_csv(self.expected_output_file)
        # self.assertEqual(len(output_df), expected_row_count)
        # self.assertEqual(output_df['some_column'].iloc[0], 'expected_value')

    def tearDown(self):
        # Clean up: Remove the output file and directory if they exist
        if os.path.isfile(self.expected_output_file):
            os.remove(self.expected_output_file)
        if os.path.isdir(os.path.dirname(self.expected_output_file)):
            os.rmdir(os.path.dirname(self.expected_output_file))


if __name__ == '__main__':
    unittest.main()

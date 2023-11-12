# CSV Data Extractor

`csv_data_extractor` is a Python package designed to efficiently process and extract specific data from CSV files. It allows users to filter records based on specified criteria, sort the data, and save the output in a structured format. The package is particularly useful for handling large datasets and automating data extraction tasks.

## Features

- Process individual CSV files or all files within a directory.
- Filter records based on specific column criteria.
- Sort data based on character counts or other custom criteria.
- Export filtered and sorted data to new CSV files.
- Handle various data types and encoding schemes.

## Installation

To install `csv_data_extractor`, simply use pip:

```bash
pip install csv_data_extractor
```

Alternatively, you can clone the repository and install the package manually:

```bash
git clone https://github.com/mohjak/csv_data_extractor.git
cd csv_data_extractor
pip install .
```

## Usage

Here's a quick example of how to use `csv_data_extractor`:

```python
from csv_data_extractor import process_csv_files

# To process a single file:
process_csv_files('path/to/your/file.csv')

# To process all files in a directory:
process_csv_files('path/to/your/directory')
```

## Requirements

- Python 3.6 or later
- pandas

## Contributing

Contributions to `csv_data_extractor` are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for instructions on how to submit changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any queries or feedback, please contact [Mohammad Jaqmaqji](mailto:mohjak@gmail.com).

# Changelog

All notable changes to the `csv-data-extractor` project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-11-12

### Added

- Initial release of the `csv-data-extractor` package.
- Functionality to process individual CSV files or all files within a specified directory.
- Filtering of records based on specific column criteria ('وسوم داخلية').
- Sorting of data based on the character count in 'سؤال الفتوى' and 'جواب الفتوى' columns.
- Generation of a new column 'Old CMS Edit URL' based on 'Slug' values.
- Exporting of filtered and sorted data to new CSV files in a subdirectory 'out'.
- Comprehensive error handling to manage files without required columns or with incorrect formatting.
- Unit tests for validating the core functionalities of the package.

[1.0.0]: https://github.com/mohjak/csv-data-extractor/releases/tag/1.0.0

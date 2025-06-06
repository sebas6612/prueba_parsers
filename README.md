# Python Parser Project

This project is designed to parse different data types, specifically focusing on unzipping files and converting XML files to CSV format. It includes a flexible architecture that allows for easy addition of new parser types.

## Project Structure

```
python-parser-project/
├── logs/
│   └── job_processor.log
├── s3_simulation/
│   └── alejo-parsers/
│       └──workspace1/
│           └──workspace1/
│               └──sources/
│                   ├──rutafuente1/
│                   │   ├── miarchivo1.zip
│                   │   └── miarchivo2.xml
│                   └──rutafuente2/             # output folder
├── src/
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── base_parser.py      # Abstract base class for all parsers
│   │   ├── zip_parser.py       # Parser for unzipping files
│   │   └── xml_parser.py       # Parser for XML to CSV conversion
│   ├── utils/
│   │   ├── __init__.py
│   │   └── job_processor.py    # Handles job definition and execution
├── main.py                     # Entry point of the application
├── job_definition.json         # Configuration file for parsing jobs
└── README.md                   # Project documentation
```

## Features

- Abstract base parser class for consistent parser implementation
- XML to CSV conversion
- ZIP file extraction
- Configurable job processing through JSON
- Comprehensive logging system
- Error handling and recovery

## Usage

1. Define your jobs in `job_definition.json`:
```json
{
  "transformations": [
    {
      "object": {
        "origin": "path/to/source.zip",
        "destiny": "path/to/destination/",
        "parser": "unzip",
        "classname": "ZipFileParser"
      }
    }
  ]
}
```

## How to run

This project uses [uv](https://github.com/astral-sh/uv), a fast and modern Python package manager.

Follow these steps to run the project:

1. **Clone the repository**
    ```sh
    git clone https://github.com/sebas6612/prueba_parsers.git
    cd prueba_parsers
    ```

2. **Install uv**
    #### On macOS and Linux.
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    #### On Windows.
    ```sh
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

3. **Run the main script**
    ```sh
    uv run main.py
    ```

Make sure to configure your `job_definition.json` before running the script.

## Adding New Parsers

1. Create a new parser class in the `src/parsers` directory
2. Inherit from `BaseParser`
3. Implement the required `parse()` method
4. Add the parser to the `PARSER_MAPPING` in `job_processor.py`

## Requirements

- uv
- Python 3.12+

## Logging

Logs are stored in `logs/job_processor.log` and include:
- Job processing events
- Transformation status
- Errors and warnings
- Parser execution details

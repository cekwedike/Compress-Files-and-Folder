# Python Compression Tool

This Python script allows users to compress directories into various archive formats, including ZIP, TAR, and TGZ, with an easy-to-use command-line interface. When compressing into the TGZ format, the archive name is automatically generated based on the directory name and the current date.

## Features

- Compress directories into ZIP, TAR, or TGZ formats.
- Auto-generate archive names for TGZ files based on the directory name and the current date.

## Prerequisites

Before you run this script, ensure you have Python installed on your system. This script has been tested with Python 3.6 and above. No external libraries are required as it uses only standard libraries included with Python.

## Installation

No installation is needed. Just ensure you have Python installed.

## Usage

To use this tool, follow these steps:

1. **Prepare Your Directory**: Ensure the directory you want to compress is accessible and that you have the necessary permissions to read from and write to your chosen directory.

2. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the folder containing `compress_folder.py`.
    - Execute the script by running:
      ```
      python compress_folder.py
      ```
    - Follow the on-screen prompts to select the directory and compression format.

### Step-by-Step Instructions

After launching the script, you will be prompted to:

1. **Enter the path to the directory you wish to compress**: Provide the full path to your directory.

2. **Select the compression type**: Choose from the available options (1 for ZIP, 2 for TAR, 3 for TGZ).

The script will then compress the directory into the selected format and output the name of the compressed file or an error message if the process fails.

## Contributing

Your contributions are welcome! If you have suggestions for improving this script, please open an issue or pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any problems or have feedback, please open an issue on the project's GitHub page.

---

Project by Chidiebere Ekwedike

For more information or assistance, please contact c.ekwedike@alustudent.com.


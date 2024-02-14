#!/usr/bin/python3

import os
import tarfile
import zipfile
from datetime import datetime


def compress_folder(folder_path, compress_type):
    """
    Compresses a folder to the specified compression type.

    Parameters:
        folder_path (str): The path to the folder to compress.
        compress_type (str): The compression type (e.g., 'zip', 'tar', 'tgz').

    Returns:
        str: The path to the compressed file or an error message.
    """
    try:
        # Generate the filename based on the folder name and current date
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

        # Compress the folder based on the selected type
        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file),
                                   os.path.relpath(os.path.join(root, file),
                                                   os.path.join(folder_path, '..')))
        elif compress_type in ['tar', 'tgz']:
            mode = 'w:gz' if compress_type == 'tgz' else 'w'
            with tarfile.open(compressed_file_name, mode) as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))

        return f"Compression successful: {compressed_file_name}"
    except Exception as e:
        return f"Compression failed: {e}"


def main():
    folder_path = input("Enter the path to the folder you wish to compress: ")
    print("Select the compression type:")
    print("1. zip\n2. tar\n3. tgz")
    type_option = input("Enter your choice (1/2/3): ")

    compress_types = {'1': 'zip', '2': 'tar', '3': 'tgz'}
    compress_type = compress_types.get(type_option, 'zip')

    result = compress_folder(folder_path, compress_type)
    print(result)


if __name__ == "__main__":
    main()

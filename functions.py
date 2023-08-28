import zipfile


# Define a function to handle the extraction of zip file
def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(dest_dir)

# def extract_archive(filepath, dest_dir):
#     try:
#         with zipfile.ZipFile(filepath, 'r') as archive:
#              archive.extractall(dest_dir)
#              msg.update('Files extracted successfully!')
#     except FileNotFoundError:
#         sg.popup("File not found. Please provide a valid filepath.")
#     except Exception as e:
#         sg.popup(f"An error occurred: {str(e)}")



if __name__ == '__main__':
    filepath = r"C:\Users\shibb\PythonProjectsFinal\app1_zip_extract\compressed.zip"
    dest_dir = r"C:\Users\shibb\PythonProjectsFinal\app1_zip_extract\extracted_files"
    extract_archive(filepath=filepath, dest_dir=dest_dir)
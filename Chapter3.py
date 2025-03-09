import zipfile
import os

def compressFile(filePaths, outputZip):
    try:
        with zipfile.ZipFile(outputZip, 'w', zipfile.ZIP_DEFLATED) as zipFile:
            for file in filePaths:
                zipFile.write(file, os.path.basename(file))
        print(f"Files compressed into {outputZip}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def bai55():
    filePaths = ['test.txt']
    outputZip = 'test.zip'
    compressFile(filePaths, outputZip)
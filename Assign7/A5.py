import os

fileName = input("Enter the filename: ")

if os.path.exists(fileName):
    fileStat = os.stat(fileName)
    print(f"File Name: {fileName}")
    print(f"Size (in bytes): {fileStat.st_size}")
    print(f"Last Modified Time: {fileStat.st_mtime}")
    print(f"File Mode: {oct(fileStat.st_mode)}")

else:
    print(f"'{fileName}' not found")

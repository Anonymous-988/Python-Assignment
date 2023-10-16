import os

inputFile = input("Enter a filename to search: ")

# Using recursive file search, searches in multiple level
fileFound = False

for root, dir, files in os.walk(os.getcwd):
    if inputFile in files:
        print(f"{inputFile} found at {root}")
        fileFound = True

if not fileFound:
    print(f"{inputFile} not found")

# Using listDir, searches in single level
fileList = os.listdir()
if inputFile in fileList:
    print(f"{inputFile} found at {os.getcwd()}")
else:
    print(f"{inputFile} not found")
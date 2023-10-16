import os

inputDir = input("Enter directory name: ")

# List files in the specified directory
fileList = os.listdir(inputDir)

# Create a dictionary to organize files by extension
fileExtensionList = {}

for file in fileList:
    if os.path.isfile(os.path.join(inputDir, file)):
        fileName, fileExtension = os.path.splitext(file)
        fileExtension = fileExtension.lower()  # Normalize the extension to lowercase
        if fileExtension not in fileExtensionList:
            fileExtensionList[fileExtension] = []
        fileExtensionList[fileExtension].append(file)

# Print files organized by extension
for extension, files in fileExtensionList.items():
    print(f"Files with extension {extension}:")
    for file in files:
        print(f"- {file}")
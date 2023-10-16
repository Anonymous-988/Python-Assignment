import os

inputDir = input("Enter a Directory Name: ")

fileList = os.listdir(inputDir)

extensionMap = {}

for file in fileList:
    # this somehow didnt work for os.path.isfile(file)
    if os.path.isfile(os.path.join(inputDir, file)):
        fileName, fileExtension = os.path.splitext(file)
        fileExtension = fileExtension.lower()
        if fileExtension not in extensionMap:
            extensionMap[fileExtension] = 1
            continue
        extensionMap[fileExtension] += 1

# print(extensionMap)

for key in extensionMap:
    print(f"{key} file count: {extensionMap[key]}")
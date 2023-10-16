import os

inputDir = input("Enter Directory Name: ").strip()

if inputDir == '':
    fileList = os.listdir()
else:
    fileList = os.listdir(inputDir)

for file in fileList:
    print(file)
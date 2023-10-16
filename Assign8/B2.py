import os

inputDir = input("Enter a directory name: ")

print("All files within the dir {inputDir} are:")

for root, dirs, files in os.walk(inputDir):
    for file in files:
        filePath = os.path.join(root, file)
        print(f"{file} => {filePath}")
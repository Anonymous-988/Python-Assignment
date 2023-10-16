import os

inputDir = input("Enter Directory Name to create: ")
os.mkdir(inputDir)

newDir = input("Enter new name to rename: ")
os.rename(inputDir, newDir)

input("----Please enter to delete the directory----")
os.rmdir(newDir)
print(f"{newDir} is deleted")
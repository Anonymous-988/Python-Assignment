import os

sourceDir = input("Enter a source dir: ")
destinationDir = input("Enter a destination dir: ")

for filename in os.listdir(sourceDir):
    sourceFile = os.path.join(sourceDir, filename)
    destinationFile = os.path.join(destinationDir, filename)

    if os.path.isfile(sourceFile):
        with open(sourceFile, 'rb') as source:
            with open(destinationFile, 'wb') as destination:
                destination.write(source.read())
        
        print(f"File '{filename}' copied to the destination directory.")

print("All files have been copied.")
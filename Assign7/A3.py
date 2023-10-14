inputSource = input("Source File ? ")
inputDestination = input("Destination File ? ")

with open(inputSource, 'r') as source, open(inputDestination, 'w') as destination:
    destination.write(source.read())

print("{inputSource} copied into {inputDestination}")
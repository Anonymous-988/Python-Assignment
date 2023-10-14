with open("A1.txt",'w') as file:
    print("Enter your message line by line")
    for i in range(5):
        inputLine = input("")
        if i == 4:
            file.write(inputLine)
            break
        file.write(inputLine + "\n")

print("Message added in A1.txt file")
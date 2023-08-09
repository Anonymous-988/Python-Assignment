str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

# temp = str1[:2]
# str1 = str2[:2] + str1[2:]
# str2 = temp + str2[2:]

str1, str2 = str2[:2] + str1[2:], str1[:2] + str2[2:]

print(f"New String: {str1+str2}")

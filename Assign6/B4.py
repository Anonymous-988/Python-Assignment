def toBinary(num):
    if num == 0:
        return '0b0'  # Binary representation of 0 is '0b0'

    binaryStr = ''
    while num > 0:
        binaryStr = str(num % 2) + binaryStr
        num //= 2

    return '0b' + binaryStr

def toOctal(num):
    if num == 0:
        return '0o0'  # Octal representation of 0 is '0o0'

    octalStr = ''
    while num > 0:
        octalStr = str(num % 8) + octalStr
        num //= 8

    return '0o' + octalStr

def toHexa(num):
    if num == 0:
        return '0x0'  # Hexadecimal representation of 0 is '0x0'

    hexaStr = ''
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hexaStr = str(remainder) + hexaStr
        else:
            # Map values 10-15 to A-F for hexadecimal representation
            hexaStr = chr(ord('A') + remainder - 10) + hexaStr
        num //= 16

    return '0x' + hexaStr

inputNum = int(input("Enter a decimal number: "))
print(f"Binary of {inputNum} is {toBinary(inputNum)}")
print(f"Octal of {inputNum} is {toOctal(inputNum)}")
print(f"Hexadecimal of {inputNum} is {toHexa(inputNum)}")
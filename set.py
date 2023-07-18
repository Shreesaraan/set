def set(number, bit):
    result=0  
    result|=(1<<number)
    result|=(1<<bit)
    return result

number=int(input("Enter the Number : "))
bit=int(input("Enter the Bit to Set : "))
print(set(number,bit))
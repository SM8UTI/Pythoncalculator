"""
author      : Smruti Ranjan Nayak
Github Link : https://github.com/SmrutiRN
"""
sym = "*"
print(sym * 45)
x = int(input("[1] First Number  : "))
y = int(input("[2] Second Number : "))
print(sym * 45)
z = """
    [+] Add 
    [-] Subtracts
    [/] Divides
    [*] Multiplies
    

"""
print (z)
action = str(input("Enter your Choice(EX : + , - ): "))
print(sym * 45)

if action == "+":
    add = int(x + y)
    print("[+] Your Value : ",add)
    print(sym * 45)
elif action == "-":
    substract = int(x - y)
    print("[-] Your Value :",substract)
    print(sym * 45
elif action == "*":
    multiplies = int(x * y)
    print("[*] Your Value :",multiplies)
    print(sym * 45
elif action == "/":
    divide = int(x / y)
    print("[/] Your Value :",divide)
    print(sym * 45
else:

    print("Plz choice wright option ? ")
    print(sym * 45











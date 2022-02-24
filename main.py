
print("This program converts decimal numbers to their binary, octal and hexadecimal equivalents")
number = int(input("Enter number here : "))
choice = input("Binary(B) or Octal(O)? or Hexadecimal(H): ").upper()

oct = []
bin = []
hex = []
if choice == "B":
    for i in range(0, 100):
        rem = number % 2
        number = number // 2
        bin.append(rem)
        if number <= 0:
            break
    bin.reverse()
    print(bin)
elif choice == "O":
    for i in range(0, 100):
        rem = number % 8
        number = number // 8
        oct.append(rem)
        if number <= 0:
            break
    oct.reverse()
    print(oct)
elif choice == "H":
    obj = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    for i in range(0, 100):
        rem = number % 16
        if rem > 9:
            hex.append(obj[rem])
        else:
            hex.append(rem)
        number = number // 16
        if number <= 0:
            break
    hex.reverse()
    print(hex)


else:
    print("Enter valid choice!")



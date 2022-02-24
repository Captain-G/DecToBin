
print("This program converts decimal numbers to their binary or octal equivalents")
number = int(input("Enter number here : "))
choice = input("Binary(B) or Octal(O)? : ").upper()

oct = []
bin = []
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
else:
    print("Enter valid choice!")



print("This program converts decimal numbers to their binary equivalent")
number = int(input("Enter number here : "))

bin = []
for i in range(0, 100):
    rem = number % 2
    number = number // 2
    bin.append(rem)
    if number <= 0:
        break
bin.reverse()
print(bin)


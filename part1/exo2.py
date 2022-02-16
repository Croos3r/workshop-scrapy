from sys import argv

i: int = int(argv[1])
number: list[int] = [int(char) for char in str(i)]

for i in range(len(number)):
    number.append(number[i] * number[i + 1])

number.sort()
for i in range(len(number)):
    if i != len(number) - 1 and number[i] == number[i + 1]:
        print(f"{argv[1]} --> false")
        exit()
print(f"{argv[1]} --> true")
from sys import argv

if len(argv) != 3:
    print("Incorrect number of arguments")
    print("Usage: python question_01.py num1 num2")
    exit(0)

number1 = float(argv[1])  # convert to float
number2 = float(argv[2])  # convert to float

result1 = number1 + number2
print(f"{number1} + {number2} = {result1}")
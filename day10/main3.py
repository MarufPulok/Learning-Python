def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

operations = {"+" : add ,"-" : subtract,"*" : multiply, "/" : divide}


num1 = int(input("What's The first Number: "))



for symbol in operations:
  print(symbol)

operationSymbol = input("Choose Operation from above: ")

num2 = int(input("What's The second Number: "))

calculation_function = operations[operationSymbol]
result = calculation_function(num1, num2)
print(f"{num1} {operationSymbol} {num2} = {result}")
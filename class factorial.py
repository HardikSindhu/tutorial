#write a program using a class to genrate the factorial of any no. supply by the user
class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        return factorial
number = int(input("Enter a number: "))
fact = Factorial(number)
print("The factorial of", number, "is", fact.calculate())

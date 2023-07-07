num = list(map(int,input("provide a list : ").split(' ')))

squared = list(map(lambda x: x ** 2, num))

print("Given numbers:", num)
print("Squared numbers:", squared)
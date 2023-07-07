def triple(num):
    return num * 3

num = list(map(int,input("provide a list : ").split(' ')))
tripled = list(map(triple, num))

print("Given numbers:", num)
print("Tripled numbers: ", tripled)
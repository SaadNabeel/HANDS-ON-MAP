
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]


additionresult = list(map(lambda x, y: x + y, numbers1, numbers2))

print("Addition of numbers from two different lists:")
print(additionresult)


nums = [1, 2, 3, 4, 5]


squareresult = list(map(lambda x: x ** 2, nums))

print("Square of numbers from the list:")
print(squareresult)


# According to question first making perfect function and then applying filter

perfect = lambda num1: num1 == sum(list(filter((lambda val: num1 % val == 0), range(1, (num1 // 2) + 1))))

# iter can be any iterable: e.g: list of items or a range value like in our case
iter = range(1, 10000)

ans = list(filter(perfect, iter))
print(ans)



""" 
# A one liner code (modified)

perfect = lambda iter: list(filter((lambda num1: num1 == sum(list(filter((lambda val: num1 % val == 0), range(1, (num1 // 2) + 1))))), iter))

# Now calling the perfect function with argument
print(perfect(range(1, 10000)))

"""

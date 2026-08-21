#4-3 Counting to Twenty
for value in range(1, 21):
    print(value)

# #One Million
numbers = list(range(1, 1000001))

for number in numbers:
 print(number)

 #Summing a Million
 numbers = list(range(1, 1000001))
 print(sum(numbers))

# #Odd Numbers
 odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

# #threes
threes = list(range(3, 31, 3))
print(threes)

for number in threes:
    print(number)


 #cubes
cubes = []

# for value in range(1, 10):
cube = value**3
cubes.append(cube)

print(cubes)

#Cube Comprehension
cubes = [value**3 for value in range(1, 10)]
print(cubes)


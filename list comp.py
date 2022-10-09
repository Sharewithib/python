#list comp
l = []

for letter in 'python':
    l.append(letter)
print(l)
#iter
#Example 2: Iterating through a string
#Using List Comprehension

l1 = [ l for l in 'python' ]
print( l1)

l2 = list(map(lambda x: x, 'python'))
print(l2)
#direct
#Conditionals in List Comprehension
l3 = [ x for x in range(20) if x % 2 == 0]
print(l3)
#Nested IF with List Comprehension
l4 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(l4)
#if...else With List Comprehension
l5 = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(l5)
#Nested Loops in List Comprehension

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

#singleline cmd
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

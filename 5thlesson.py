words = ['apple', 'banana', 'apple', 'cherry', 'banana']
unique_words = {word for word in words}
print(unique_words)

even_numbers = {x for x in range(10) if x%2==0}
print(even_numbers)

sentence = "Python programming language is awesome"
vowels = {char for char in sentence if char in 'aeiouAEIOU'}
print(vowels)

# #bir xil narsa
numbers = [1,2,3,4,5,6,6,7,7,8,9]
evens = {even for even in numbers if even%2==0}
print(evens)
#bir xil narsa
input_list =[1,2,3,4,5,6,7,8,9]
output_list =set()

for var in input_list:
    if var%2==0:
        output_list.add(var)
print(output_list)


#problems in class

#5
s = set()
for i in range(0,20,2):
    s.add(i)
for i in range(0,20,3):
    s.discard(i)
print(s)
#4
s = set()
for i in range(1,5):
    s.add(i*i)
    s.add(-i)
print(s)
#3

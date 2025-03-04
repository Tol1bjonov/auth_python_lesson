#1
# squeares = {x: x**2 for x in range(5)}
# print(squeares)
#
# even_square = {y: y**2 for y in range(10) if y%2 ==0}
# print(even_square)

#2
# original = {'a': 1, 'b': 2, 'c':3}
# inverted = {v: k for k, v in original.items()}
# print(inverted)
#
# parity = {x: "even" if x%2==0 else "Odd" for x in range(5)}
# print(parity)

#3
# words = ["apple", "banana", "cherry"]
# word_length = {word: len(word) for word in words}
# print(word_length)
#
# nested_dict = {x: {y:y**2 for y in range(3)} for x in range(2)}
# print(nested_dict)

#4
# input_list = [1,2,3,4,5,6,7,8,9]
# output_dict={}
# for var in input_list:
#     if var%2!=0:
#         output_dict[var]=var**3
# print(output_dict)

#5
# input_list = [1,2,3,4,5,6,7]
# dict_comp = {var: var**3 for var in input_list if var%2!=0}
# print(dict_comp)


#6
states = ["California", "Texas", "Florida", "New York"]
capitals = ["Sacramento", "Austin", "Tallahassee", "Albany"]
state_dict = {}
for i in range(len(states)):
    state_dict[states[i]] = capitals[i]
print(state_dict)

state_capital_dict = {states[i]: capitals[i] for i in range(len(states))}
print(state_capital_dict)

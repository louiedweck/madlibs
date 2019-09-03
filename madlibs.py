input_types = ['plural animal', 'noun', 'adjective', 'verb', 'name', 'noun', 'verb', 'adverb', 'noun', 'adjective']
user_inputs = []

for input_type in input_types:
    user_input = input('Enter a(n) ' + input_type + ': ')
    user_inputs.append(user_input)


# print(user_inputs)

story = 'One day three ' + user_inputs[0] + ' saw a ' + user_inputs[1] + ''
print(story)
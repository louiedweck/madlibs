input_types = ['plural animal', 'noun','verb', 'adverb', 'name', 'noun', 'verb', 'adverb', 'noun', 'adjective']
user_inputs = []

for input_type in input_types:
    user_input = input('Enter a(n) ' + input_type + ': ')
    user_inputs.append(user_input)


# print(user_inputs)

story = 'One day three ' + user_inputs[0] + ' saw a ' + user_inputs[1] + user_input[2] + ' frolicking ' + user_input[3] + 'though the woods to ' + user_input[4] + "'s house. " + 
print(story)
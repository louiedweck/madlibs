input_types = ['plural animal', 'different plural animal',
               'verb', 'adverb', 'name', 'verb']
user_inputs = []

for input_type in input_types:
    user_input = input('Enter a(n) ' + input_type + ': ')
    user_inputs.append(user_input)


# print(user_inputs)

story = 'One day three ' + user_inputs[0] + ' saw a group of ' + user_inputs[1] + ' ' + user_inputs[2] + ' and frolicking ' + user_inputs[3] + ' through the woods to the house of ' + user_inputs[4] + \
    '. But on their way through the forest, they were attacked by a group of viscous baboons ' + \
        user_inputs[5] + '. ' + \
    ' Thankfully everyone was unscathed and ventured back home. If only they knew what they had in store next. Little did they know ______ wre lurking behind them. '
print(story)

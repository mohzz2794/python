# asks the user to enter their names and ages

name = input('Enter your name: ')
age = input('Enter your age: ')

# print a message to show the year that they will ture 100 years old

year = 2018 - int(age) + 100
message = name + ' will be 100 years old in ' + str(year) + '\n'
print(message)

#Close the screen after input

finish = input('Press Enter')

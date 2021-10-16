# a program that prints out all the elements of the list that are less than 5.
# Take this list, a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("pick a number:"))
new_list = []
for item in a:
    if item < number:
        new_list.append(item)
        print(new_list)
        
        end_program = input("Press enter")
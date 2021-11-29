# Make a program with list
print("Issue a value at Day_one:")
Day_one = ['Chicken', 'Bread', 'Milk']
print(Day_one)

print('/n')

print("Use for in on list")
for menu in Day_one:
    print(menu)

print('/n')

print("Issue values in the list one by one")
print(Day_one[0])

print('/n')

print("Expand the list")
Day_one = [12, 'Chicken', 'Bread', 'Milk', 'panda']
for i in range(0, len(Day_one)):
    print(Day_one[i])

print('/n')

print("Add a value in list")
Day_one.append('crocodile')
print(Day_one)

print('/n')

Day_one.clear()

print('/n')
Day_one = [12, 'Chicken', 'Bread', 'Milk', 'panda']
Day_one.pop(2)
for i in range(0, len(Day_one)):
    print(Day_one[i])

print('/n')
Day_one = [12, 'Chicken', 'Bread', 'Milk', 'panda']
Day_one.pop()
for i in range(0, len(Day_one)):
    print(Day_one[i])

print('/n')
Day_one = [12, 'Chicken', 'Bread', 'Milk', 'panda']
Day_one[0] = 'Godzila'
for i in range(0, len(Day_one)):
    print(Day_one[i])

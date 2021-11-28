# Sequential and looping (while undefined count)
print('Arman Receives orders from mom, to make 10 coffee')
print('Arman obeyed mom orders, then rushed to make 10 coffee')

amount_of_coffee = 10

total_coffee = 0

Coffee_that_has_been_made_and_tasted = 0


print('Coffee in the making process')

while total_coffee < amount_of_coffee:
    total_coffee = total_coffee + 1

    if Coffee_that_has_been_made_and_tasted == 9:
        print(f'Coffee {Coffee_that_has_been_made_and_tasted + 1} has not been sugar and not worth it to served')
    else:
        Coffee_that_has_been_made_and_tasted = Coffee_that_has_been_made_and_tasted + 1
        print(f'Coffee {Coffee_that_has_been_made_and_tasted} has been sugar and worth it to served')

print(f'Arman said to mom: "Mom I can only make a {Coffee_that_has_been_made_and_tasted} coffee"')

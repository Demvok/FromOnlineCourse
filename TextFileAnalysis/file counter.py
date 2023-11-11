lst = []
with open('file.txt') as file:
    for row in file:
        lst.append(row.strip())

letters = sum([ sum( [ len([symb for symb in word if symb.isalpha()]) for word in row.split() ] ) for row in lst ])
words = sum([ len([ word for word in row.split() ]) for row in lst ])
lines = len(lst)

print('Input file contains:')
print(f'{letters} letters')
print(f'{words} words')
print(f'{lines} lines')
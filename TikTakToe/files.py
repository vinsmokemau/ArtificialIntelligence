"""Script to modify a txt file."""
file = open("sequences.txt", "a")

list_2_write = [5, 9, 3, 7, 1, 2, 6, 8, 4]

list_2_write = [str(number) for number in list_2_write]

file.write('[{}]\n'.format(','.join(list_2_write)))

file.close()

words = input('Enter the words: ')
words_list = words.split()
separator = '_'
new_string = separator.join(words_list)
print('New string: ', new_string)


example_list = ['a','funny','story']



char_tuples = map(tuple,example_list)


for item in char_tuples:
    print(item)


list(map(print,example_list))


fruit_file = open('fruit.txt', 'r')

list(map(print,map(str.upper,map(str.strip,fruit_file))))


import operator

example_tuples_list = [('Apple', 16), ('Banana', 12), ('Orange', 7), ('Grapes', 30)]

sorted_tuples = sorted(example_tuples_list, key = operator.itemgetter(1))

list(map(print,sorted_tuples))
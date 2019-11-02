from functools import reduce
import operator

example_string_list = ['a','funny','story','dsafadsda','fdsrt','fdsfsdg']

##1
char_num = reduce(lambda tot,curr: tot+len(curr),example_string_list,0)
print(char_num)

char_num = len(reduce(operator.add,example_string_list))

print(char_num)

##2
char_num = reduce(operator.add,map(len,example_string_list))

print(char_num)


##2
char_num = sum(map(len,example_string_list))

print(char_num)
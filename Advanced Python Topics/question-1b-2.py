
import collections

text_to_count = "Man is fond of counting his troubles, but he does not count his joys. If he counted them upas \
he ought to, he would see that every lot has enough happiness provided for it."



#Main


file_object  = open("Advanced Python Topics - Lab Files/2b-functional_tools/fruit.txt", 'r')

text_to_count = file_object.read()
word_list = text_to_count.split()
c = collections.Counter()
print('Initial :{}', format(c))

c.update(word_list)
print('Common :{}', format(c.most_common(10)))
print('Uncommon :{}', format(c.most_common()[-10:]))
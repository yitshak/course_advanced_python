
import collections

text_to_count = "Man is fond of counting his troubles, but he does not count his joys. If he counted them upas \
he ought to, he would see that every lot has enough happiness provided for it."



#Main



c = collections.Counter()
print('Initial :{}', format(c))

c.update(text_to_count)
print('Final :{}', format(c))
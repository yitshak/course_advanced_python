
import collections
import csv
from collections import namedtuple


#Main


with open("Advanced Python Topics - Lab Files/1b-specialised_data_structures/us-500.csv",'r') as file_content:
    file_reader = csv.reader(file_content)


    UserRecord = namedtuple('UserRecord',next(file_reader))

    record_list = []
    for line in file_reader:
        line_tuple = UserRecord(*line)
        record_list.append([line_tuple.first_name + ' ' + line_tuple.last_name, line_tuple.email])


    print ("{:<30}{:30}".format("Name","E-mail"))
    for record in record_list:
        print("{:<30}{:30}".format(record[0],record[1]))

##text_to_count = file_object.read()
##word_list = text_to_count.split()
##c = collections.Counter()
##print('Initial :{}', format(c))
##
##c.update(word_list)
##print('Common :{}', format(c.most_common(10)))
##print('Uncommon :{}', format(c.most_common()[-10:]))










prefix = input("Please enter fruit prefix:   \n")


print("\n\n2\n")
with open("Advanced Python Topics - Lab Files/2b-functional_tools/fruit.txt") as fruit_file:
    selected_fruits = map(lambda x:  x.strip().upper(),
                          filter( lambda x: x.lower().startswith(prefix.lower()), fruit_file))
    print(list(selected_fruits))

print("\n\n3\n")
with open("Advanced Python Topics - Lab Files/2b-functional_tools/fruit.txt") as fruit_file:
    selected_fruits = ( x.strip().upper() for x in fruit_file if x.strip().lower().startswith(prefix.lower()))
    print(list(selected_fruits))

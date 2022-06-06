# SOURCE ---- https://www.geeksforgeeks.org/iterate-through-list-of-dictionaries-in-python/
# Create a function iterateDictionary(some_list)
# given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

students = [
   {'first_name':  'Michael', 'last_name': 'Jordan'},
   {'first_name': 'John', 'last_name': 'Rosales'},
   {'first_name': 'Mark', 'last_name': 'Guillen'},
   {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Wasn't able to get them side by side 
def iterateDictionary(list_var):
   for i in range(len(list_var)):
      for key, val in list_var[i].items():
         first_value = "{} - {}".format(key, val)
         print(first_value)
iterateDictionary(students)

# Number Three
print("")
print("")
def iterateDictionary2(key_name, some_list):
   for i in some_list:
      name = list(i.keys())[0]
      if key_name == name:
         print_name = list(i.values())[0]
         print(print_name)

      second_name = list(i.keys())[1]
      if key_name == second_name:
         print_name = list(i.values())[1]
         print(print_name)

iterateDictionary2('first_name', students)
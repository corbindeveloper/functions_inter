# Create a function that given a dictionary whose values are all lists
# Prints the name of each key along with the size of its list and then prints the associated values within each key's list

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
   for key, val in some_dict.items():
      print(str(len(val)) + " {}".format(key))
      for i in val:
         print("{}".format(i))
      print("")

printInfo(dojo)


#Part III - Dictionary

filename = 'faculty.csv'
f = open(filename)
f_lines = f.readlines() # list of strings

f_lines = [x.strip() for x in f_lines] # getting rid of \n at the end of each line

f_list = [] # a list to store values of each line in the file
faculty_dict = {}
professor_dict ={}

for i in range(1,len(f_lines)):
    faculty_member = []
    professor_member =[]
    f_list = list(f_lines[i].split(','))

    names =  list(f_list[0].split(' ')) # a list of names (first, middle, last)

    faculty_member.append(names[-1]) # contains last name only
    faculty_member.append(f_list[1])
    faculty_member.append(f_list[2])
    faculty_member.append(f_list[3])
    faculty_dict.setdefault(faculty_member[0],[]).append(faculty_member[1:])

    professor_member.append((names[0],names[-1])) # contains both first and last names
    professor_dict.setdefault(professor_member[0],[]).append(faculty_member[1:])

    #When setdefault() is called, it will check if the key already exists.
    #If it does exist, then setdefault() does nothing.
    #If the key does not exist, then setdefault() creates it and sets it
    #to the value specified in the second argument.

print("-"*10)
print("Q6. Create a dictionary where key is represented by the last name of the faculty members.")
for key in faculty_dict:
    print("%s: %r" % (key, faculty_dict[key]))
# another way to print my dictionary line by line is pprint.pprint(faculty_dict),
#but the output wasn't exactly how I wanted it to be.

print("-"*10)
print("Q7. Create a dictionary where key is represented by professors' first and last names.")
print("Print values in alphabetical order sorted by the first names.")
professor_dict_firstname = sorted(professor_dict.items(), key=lambda t: t[0][0])
# dict.items returns tuples of form (key, value)
for key in professor_dict_firstname:
    print(key)

print("-"*10)
print("Q8. Create a dictionary where key is represented by professors' first and last names.")
print("Print values in alphabetical order sorted by the last names.")
professor_dict_lastname = sorted(professor_dict.items(), key=lambda t: t[0][1])
# dict.items returns tuples of form (key, value)
for key in professor_dict_lastname:
    print(key)

f.close()

# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

filename = 'dsp/python/football.csv'
f = open(filename)
f_lines = f.readlines() # list of strings

f_lines = [x.strip() for x in f_lines] # getting rid of \n at the end of each line

f_list = [] # a list to store values of each line
f_result = [] # a list to store tuples with names of the teams and diff b/w their goals
for i in range(1,len(f_lines)):
    f_list = list(f_lines[i].split(','))
    diff = abs(int(f_list[5]) - int(f_list[6]))
    f_result.append((f_list[0],diff))

f_result_sorted = sorted(f_result, key=lambda last_el: last_el[-1])
#print(f_result_sorted)
print("The name of the team with smallest diffrence in 'for' and 'against' goals is: ")
print(f_result_sorted[0][0])
print("The difference is: ",f_result_sorted[0][1])
f.close()


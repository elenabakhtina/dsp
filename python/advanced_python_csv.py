# Part II - Write to CSV File
#Q5. Write email addresses from Part I to csv file
#Create emails.csv file, then add and commit it to your forked repository.

filename_out = "emails.csv"
f_out = open(filename_out,"w")

filename = 'faculty.csv'
f = open(filename)
f_lines = f.readlines() # list of strings

f_lines = [x.strip() for x in f_lines] # getting rid of \n at the end of each line

f_list = [] # a list to store values of each line in the file
f_emails = [] # a list to store email addresses

for i in range(1,len(f_lines)):
    f_list = list(f_lines[i].split(','))
    f_emails.append(f_list[3])

for email in sorted(set(f_emails)):
    f_out.write(email+"\n")

f.close()
f_out.close()

# Advanced Python: Part I - Regular Expressions
#Q1. Find how many different degrees there are, and their frequencies
#Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

#Q2. Find how many different titles there are, and their frequencies.
#Ex: Assistant Professor, Professor

#Q3. Search for email addresses and put them in a list.
#Print the list of email addresses.

#Q4. Find how many different email domains there are
#Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.
#Print the list of unique email domains.

import re
filename = 'faculty.csv'
f = open(filename)
f_lines = f.readlines() # list of strings

f_lines = [x.strip() for x in f_lines] # getting rid of \n at the end of each line

f_list = [] # a list to store values of each line in the file
f_degrees =[] # a list to store degrees
f_cleanDegrees =[] # a list to store degrees without spaces and dots
f_titles = [] # a list to store titles
f_emails = [] # a list to store email addresses
f_domains = [] # a list to store email domains
for i in range(1,len(f_lines)):
    f_list = list(f_lines[i].split(','))
    cleanDegree = re.sub('\W+','',f_list[1])
    f_degrees.append(f_list[1])
    f_cleanDegrees.append(cleanDegree)
    f_titles.append(f_list[2])
    f_emails.append(f_list[3])
    domain = re.findall(r'@([\w.]+)',f_list[3])
    if domain in f_domains:
        pass
    else:
        f_domains.append(domain)

print("-"*10)
print("Q1. There are %d differently spelled degrees in the data file:" % len(set(f_degrees)))
print(sorted(set(f_degrees)))

print("-"*10)
print("Q1. There are %d unique degrees in the data file:"  % len(set(f_cleanDegrees)))
print(sorted(set(f_cleanDegrees)))

print("-"*10)
print("Q2. There are %d differently spelled titles in data the file:" % len(set(f_titles)))
i=1
for title in sorted(set(f_titles)):
    print("%d. %s" %(i, title))
    i = i + 1

print("-"*10)
print("Q3. There are %d unique email addresses in the data file:" % len(set(f_emails)))
i=1
for email in sorted(set(f_emails)):
    print("%d. %s" %(i, email))
    i = i + 1

print("-"*10)
print("Q4. There are %d email domains in the file:"  % len(f_domains))
i=1
for domain in sorted(f_domains):
    print("%d. %s" %(i, domain))
    i = i + 1

f.close()
    

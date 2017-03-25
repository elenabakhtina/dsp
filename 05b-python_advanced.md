# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> Q1. There are 11 differently spelled degrees in the data file:  
[' B.S.Ed. M.S. Ph.D.', ' JD MA MPH MS PhD', ' MD MPH Ph.D', ' Ph.D', ' Ph.D.', ' PhD', ' PhD ScD', ' Sc.D.', ' ScD', '0', 'Ph.D.']

----------

>> Q1. There are 7 unique degrees from the data file:
['0', 'BSEdMSPhD', 'JDMAMPHMSPhD', 'MDMPHPhD', 'PhD', 'PhDScD', 'ScD']


#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> Q2. There are 4 differently spelled titles in data the file:  
1. Assistant Professor is Biostatistics  
2. Assistant Professor of Biostatistics  
3. Associate Professor of Biostatistics  
4. Professor of Biostatistics


#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> Q3. There are 37 unique email addresses in the data file:
1. alisaste@mail.med.upenn.edu
2. atroxel@mail.med.upenn.edu
3. bcfrench@mail.med.upenn.edu
4. bellamys@mail.med.upenn.edu
5. bryanma@upenn.edu
6. dxie@upenn.edu
7. hongzhe@upenn.edu
8. hshou@mail.med.upenn.edu
9. hsu9@mail.med.upenn.edu
10. jaroy@mail.med.upenn.edu
11. jellenbe@mail.med.upenn.edu
12. jinboche@upenn.edu
13. jrlandis@mail.med.upenn.edu
14. jshults@mail.med.upenn.edu
15. knashawn@mail.med.upenn.edu
16. liy3@email.chop.edu
17. michross@upenn.edu
18. mingyao@mail.med.upenn.edu
19. mjoffe@mail.med.upenn.edu
20. mputt@mail.med.upenn.edu
21. msammel@cceb.med.upenn.edu
22. nanditam@mail.med.upenn.edu
23. pgimotty@upenn.edu
24. propert@mail.med.upenn.edu
25. rhubb@mail.med.upenn.edu
26. rlocalio@upenn.edu
27. rshi@mail.med.upenn.edu
28. ruifeng@upenn.edu
29. rxiao@mail.med.upenn.edu
30. sellenbe@upenn.edu
31. shawp@upenn.edu
32. sratclif@upenn.edu
33. sxie@mail.med.upenn.edu
34. warren@upenn.edu
35. weiyang@mail.med.upenn.edu
36. wguo@mail.med.upenn.edu
37. whwang@mail.med.upenn.edu


#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> Q4. There are 4 email domains in the file:
1. ['cceb.med.upenn.edu']
2. ['email.chop.edu']
3. ['mail.med.upenn.edu']
4. ['upenn.edu']

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> There 5 first key to demonstrate the key 'Ellenberg' which has two values  
>>> Bellamy: [[' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']]  
>>> Bilker: [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']]  
>>> Bryan: [[' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']]  
>>> Chen: [[' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']]  
>>> Ellenberg: [[' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu'], [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu']]

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> REPLACE THIS WITH YOUR RESPONSE

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)


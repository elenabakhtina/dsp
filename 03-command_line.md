# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. **cat F1.txt > F2.txt** redirects output from the file F1 to the file F2 replacing the content of F2; **cat F1.txt >> F2.txt** adds content of F1 to the existing content of F2.
> > 2. **sort F1.txt | wc** sorts the lines of F1; The **|** then takes the standard output of the **sort** command on the left and pipes it as standard input to the **wc** command on the right. **wc** command outputs the number of lines, words, and characters in F1.
> > 3. **uniq** filters out *adjacent*, duplicate lines in a file. If two lines are the same but don't follow one another directly, the **uniq** command won't do anything with them. That's why it's better to sort the file before using **uniq** command, such as in **sort F1.txt | uniq**.
> > 4. **sed 's/white/black/' F1.txt** acts like a find-and-replace command; **sed** stands for "stream editor", **s** for "substitution". In this case, we search for the text string *white* and replace it with the string *black*. Importantly, the above command will only replace the first instance of *white* on each line. To replace *all* instances, we need to use **sed 's/white/black/g' F1.txt** where **g** stands for "global".
> > 5. **grep Black F1.txt** searches F1 for lines that match a pattern, "Black" in our case, and returns the results. It is case sensitive. **grep -i Black F1.txt** is case incentive; **grep -R pattern dir** searches files in the dirictory **dir** and returns filenames and lines in files that match the **pattern**; **grep -Rl pattern dir** searches files in the dirictory **dir** and returns only filenames that match the **pattern**.
> > 6. **rm F1.txt** deletes the file F1; **rm -r VeryImportantDir** deletes the directory and all its child directories.  
> > 7. **cp * dir/** copies all of the files in the current directory to the directory **dir**; **cp F*.txt dir/*** selects all files in the working directory starting with **F** and ending with **.txt**, and copies them to **dir**.
> > 8. **nano ~/.bash_profile** ususe **nano** terminal editor to open the *bash profile* file that stores environment settings; **alias pd="pwd"** if added to the *bash profile* file creates keyboard shortcuts, or aliases, for commonly used commands, for example **pwd**.
> > 9. **head -10 F1.txt** shows 10 first lines from the file F1; **less F1.txt** (to quit, hit q) and **more F1.txt** are also used to look at the contents of a file.
> > 10. **man grep** and **help dir** are two commands to get help on command line commands.


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 


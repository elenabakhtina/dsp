# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> my_list = [0,1,2,3,4]  
>> my_tuple = (0,1,2,3,4)  
>> **Similarities:**  
>> 1. Both lists and tuples belong to *sequence data types* which means their elements are ordered in a defined sequence and can be accessed via indices.  
>> 2. Both lists and tuples allow duplicates.    
>> 3. Both lists and tuples allow indexing, selecting, and slicing.   
my_list[0:3] - > [0, 1, 2]    
my_tuple[0:3] - > (0, 1, 2)    
>> 4. Both lists and tuples can be compared and sorted.  
my_list1 = [4,3,2,1,0] - > my_list1.sort() - > [0, 1, 2, 3, 4] #sorting  
my_tuple1 = (4,3,2,1,0) - > sorted(my_tuple1) - > [0, 1, 2, 3, 4] #sorting   
my_list > my_list1 - > False #comparing    
my_tuple < my_tuple1 - > True #comparing  
>> **Differences:**  
>> 1. Syntax. Lists use [], tuples use ()  
>> 2. Mutability. Elements in a given list are mutable and can ba changed (my_list[1] = 11 #Ok), elements in a given tuple are NOT mutable (my_tuple[1] = 11 #Error).  
>> 3. The main advantage of tuples is that they can be used as keys in dictionaries, while lists can't, becasue dictionaries require that their keys are hashable and therefore immutable.  

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A *set* is an unordered collection with no duplicate elements (lists consist of ordered elements with a define sequence and allow duplicates). Basic uses include of sets membership testing for and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.  
my_set = {0,2,4,4} - > {0, 2, 4} #sets remove duplicates, unlike lists that allow dplicates   
my_set1 = {1,3,4,4} - > {1, 3, 4}
my_set - my_set1 - > {0, 2}  #elements that are in my_set, but not in my_set1  
my_set | my_set1 - > {0, 1, 2, 3, 4}  #elements that are in either my_set or my_set1  
my_set & my_set1 - > {4}  #elements that are in both my_set and my_set1  
my_set ^ my_set1 - > {0, 1, 2, 3}  #elements that are in either my_set or my_set1 but not in both  
Similar to lists new elements can be added to sets (using the **add()** function), but they have to be immutable. Lists cannot be added to sets.  
Sets and lists are similar in a way their elements cad be added (**s.add('a')** and **l.append('a'))**, removed (**s.remove('a')** and **l.remove('a')**), and sorted (**sorted(s)** and **l.sort()**).  
Both sets and lists can check whether an element belong to them  
'a' in s - > True  
'a' in l - > True  
The big difference between lists and sets in locating elements. Not only can lists say whether an element we are looking for belong to them but also identify its exact location (by using **l.index('a')**). Because sets are collections of *unodered* elements, sets cannot locate exact positions of their elements.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called **"lambda"**. Below is an example that shows how lambda function differes from a normal function definition:
>>> def f (x): return x+10  -> print f(5)  -> 15  
>>> g = lambda x: x+10  -> print g(5)  -> 15 //Another way: (lambda x: x+10) (5)  ->  15

>> **When to use lambda function and when to use a def to create a function?** If we're going to use a function several times, or if the function is too complex to be written in a single line, then it's advisable to use a standard function. However, if we need a function only once and it's quite simple (i.e. it contains just one expression, like in the above examples), it's more convenient to use a lambda construct to generate a (temporary) anonymous function.  
>> **Other useful examples:**  
>>> l = [0,2,3,5,6,7,10,15,46]  ->  l_5 = list(filter(lambda x: x % 5 == 0, l))  ->  [0, 5, 10, 15]  
>>> cubes = list(map(lambda x: x**3, range(10)))  ->  [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
 
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.  
>> A list comprehension consists of brackets containing an expression followed by a **for** clause, then zero or more **for** or **if** clauses. The result will be a new list resulting from evaluating the expression in the context of the **for** and **if** clauses which follow it. For example,    
>>> [x+y for x in [1,2,3] for y in [10, 20, 30] if x!=1]  -> [12, 22, 32, 13, 23, 33]  

>> **Example with *map***  
>>> cubes = []  
>>> for x in range(10):  
...     cubes.append(x**3)  
... 

>>> cubes  ->  [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]  

Or, using lambda and map function: cubes = list(map(lambda x: x**3, range(10))) // yet another way: cubes = [x**3 for x in range(10)]  

>> **Example with *filter***  
>>> l = [0,2,3,5,6,7,10,15,46]  
>>> l_5 = []  
>>> for i in l:  
...     if i%5 == 0:  
...             l_5.append(i)  
... 

>>> l_5
[0, 5, 10, 15]

Or, using lambda and filter function: l_5 = list(filter(lambda x: x % 5 == 0, l))

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Here is my code  

import nsfg  
import math  
  
def CohenEffectSize(group1, group2):  
    diff = group1.mean() - group2.mean()  
    var1 = group1.var()  
    var2 = group2.var()  
    n1, n2 = len(group1), len(group2)  
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)  
    d = diff / math.sqrt(pooled_var)  
    return d  
  
preg = nsfg.ReadFemPreg()  
live = preg[preg.outcome == 1]  
firsts = live[live.birthord == 1]  
others = live[live.birthord != 1]  
  
firsts_wgt = firsts['totalwgt_lb']  
others_wgt = others['totalwgt_lb']  
  
print("Mean of the weights of first babies",firsts_wgt.mean())  
print("Mean of the weights of other babies",others_wgt.mean())  
d = CohenEffectSize(firsts_wgt, others_wgt)  
print("The difference in weights b/w first children and others using Cohen's D stats is",d)  
  
>> Mean of the weights of first babies 7.201094430437772  
>> Mean of the weights of other babies 7.325855614973262  
>> The difference in weights b/w first children and others using Cohen's D stats is -0.088672927072602  
  
>> As per internet, *Cohen suggested that d=0.2 be considered a 'small' effect size, 0.5 represents a 'medium' effect size and 0.8 a 'large' effect size.* Thus, d=0.09 is very small.

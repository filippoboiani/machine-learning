# Machine Learning
- Riccardo Sibani 
- Filippo Boiani

## Lab 1 

### Assignment 0

### Assignment 1

Entropy of the datasets: 

Dataset | Entropy 
--- | --- 
**MONK-1** | 1 
**MONK-2** | 0.957117428265
**MONK-3** | 0.999806132805

### Assignment 2
*Explain entropy for a uniform distribution and a non-uniform distribution, present some example distributions with high and low entropy.*

Entropy is the unpredictability of one event.
An uniform distribution will have an high entropy (1.0) while an non-uniform distribution will be more difficult to guess and therefore will have a low entropy. 

No distribution has high or low entropy per se. In general, discrete distributions (like binomial, poisson, uniform etc...) tend to have high entropy when the events are equiprobable. 

When the probability of a particular event is far higher then the others, the uncertainty decreases accordingly. As an example, we can the take the overly-cited toss of a coin where the sides are equals. In this case the entropy is 0 because, no matter how we toss the coin, the result will be the same. Therefore, there is no uncertainty. Entropy is not an intrinsic property of a particular distribution, but instead, it depends on the parameters. 


References: 
- [Type of distributions](http://people.stern.nyu.edu/adamodar/New_Home_Page/StatFile/statdistns.htm)
- [Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)#Introduction)

### Assignment 3

Dataset | a1 | a2 | a3 | a4 | a5 | a6 
--- | --- | --- | --- | --- | --- | --- 
**MONK-1** | 0.0752725556083 | 0.00583842996291 | 0.0047075666173 | 0.0263116965077 | 0.287030749716 | 0.000757855715864
**MONK-2** | 0.00375617737751 | 0.00245849866608 | 0.00105614771589 | 0.0156642472926 | 0.0172771769379 | 0.00624762223688
**MONK-3** | 0.00712086839607 | 0.293736173508 | 0.000831114044534 | 0.00289181728865 | 0.25591172462 | 0.0070770260741

To grow the decision tree we generally choose the alternative that bears more information reducing the uncertainty (and therefore the entropy). Given this, for MONK-1 and MONK-2 we choose a5, even though the latter doesn't have much of a gain. For MONK-3 we go for a2 which is higher than a5. 

Now we can ask ourselves why a5. Well, a5 is the set with the highest cardinality, therefore any piece of information that contributes in making the probability uneven has an higher effect on the entropy. [ASSUMPTION: CHECK]

### Assignment 4

*For splitting we choose the attribute that maximizes the information gain, Eq.3. Looking at Eq.3 how does the entropy of the subsets, Sk, look like when the information gain is maximized? How can we motivate using the information gain as a heuristic for picking an attribute for splitting? Think about reduction in entropy after the split and what the entropy implies.*

In every step we select the attribute with the most information gain. Therefore, after having selected this the entropy is minimized. The entorpy of Sk is the minimum 

### Assignment 5
### Assignment 6    
### Assignment 7    

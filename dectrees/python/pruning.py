import monkdata as m
import dtree as dtree
import drawtree_qt5 as drawLib
import random
import numpy
import matplotlib.pyplot as plt

# creates 2 partition of a dataset with random shuffling
def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

# pruning
def myPrune(tree, validation, test):
    # the tree is the current candidate
    candidate = tree
    
    # compute all the possible prunes for a tree
    newPrunes = dtree.allPruned(candidate)
    for prunedTree in newPrunes:
        # if the current candidate performs worse the another candidate
        if(dtree.check(candidate, validation) < dtree.check(prunedTree, validation)):
            candidate = myPrune(prunedTree, validation, test)
        
    # the current canditate is the best possible
    # append its classification error against the test set
    
    print "Check:       ", dtree.check(candidate, validation)
    print "TEST CHECK:  ", dtree.check(tree, test)
    # drawLib.drawTree(tree)
    return candidate


datasets = [{
    'name': 'monk1',
    'ref' : m.monk1,
    'test': m.monk1test
},
{
    'name': 'monk3',
    'ref' : m.monk3,
    'test': m.monk3test
}]

fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

results = {'monk1': [[0 for x in range(100)] for y in range(6)] , 'monk3': [[0 for x in range(100)] for y in range(6)]}
# split the dataset in training and validation set. Building
# the tree from the training set. 

for dataset in datasets: 
    print "\n\nDataset:     ", dataset['name']
    index = 0
    for f in fractions: 
        print "\n\nFraction:    ", f
        for i in range(100):
            monktrain, monkval = partition(dataset['ref'], f)
            # build the dtree from the training set
            decisionTree = dtree.buildTree(monktrain, m.attributes)
            candidate = myPrune(decisionTree, monkval, dataset['test'])
            results[dataset['name']][index][i] = dtree.check(candidate, dataset['test'])
        
        index += 1    

print "\nResults:"
print results

averages = {
    'monk1': [],
    'monk3': []
}

variances = {
    'monk1': [],
    'monk3': []
}

for x in results['monk1']:
    averages['monk1'].append(numpy.mean(x))
    variances['monk1'].append(numpy.var(x))

for x in results['monk3']:
    averages['monk3'].append(numpy.mean(x))  
    variances['monk3'].append(numpy.var(x))

print "Mean:        ", averages
print "Variances:   ", variances

plt.plot(fractions, averages['monk1'], color="blue", label="MONK-1")
plt.plot(fractions, averages['monk3'], color="red", label="MONK-3")
plt.plot(fractions, variances['monk1'], color="green", label="MONK-1")
plt.plot(fractions, variances['monk3'], color="yellow", label="MONK-3")
plt.axis([0.3, 0.8, 0, 1])
plt.ylabel('Classification Error')
plt.xlabel('Fraction')
plt.legend(loc='lower right')
plt.show()
# for i in range(0,1000000):
#     monk1train, monk1val = partition(m.monk1, 0.6)
#     # Rebuild the tree
#     decisionTree = dtree.buildTree(monk1train, m.attributes)
#     prunedTrees = dtree.allPruned(decisionTree)
#     for local in prunedTrees:
#         print local
#         print  "\n"
#         print "check = ", dtree.check(local, monk1train)
#         print "check = ", dtree.check(local, monk1val)
#         if dtree.check(local, monk1val) == 1.0:
#             print local
#             print "Check test: ", dtree.check(local, m.monk1test) # 0.972222222222
#             drawLib.drawTree(local)
#             #for sample in monk1train:
#             #    print "class = ", dtree.classify(local, sample)


# for x in range(0,6) {
#     pruned =  dtree.allPruned(decisionTree)
    
#     print ""
#     print dtree.classify(pruned[0], monk1val)

# }
    



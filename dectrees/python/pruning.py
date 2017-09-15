import monkdata as m
import dtree as dtree
import random

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

monk1train, monk1val = partition(m.monk1, 0.6)

# Rebuild the tree
decisionTree = dtree.buildTree(m.monk1, m.attributes)

print decisionTree

prunedTrees = dtree.allPruned(decisionTree)

for local in prunedTrees:
    print local
    print  "\n"
    for sample in monk1val:
        print dtree.classify(local, sample)

# for x in range(0,6) {
#     pruned =  dtree.allPruned(decisionTree)
    
#     print ""
#     print dtree.classify(pruned[0], monk1val)

# }
    



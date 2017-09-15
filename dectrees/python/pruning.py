import monkdata as m
import dtree as dtree
import drawtree_qt5 as drawLib
import random

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


monk1train, monk1val = partition(m.monk1, 0.6)
decisionTree = dtree.buildTree(monk1train, m.attributes)


def myPrune(tree):
    goalCheck = dtree.check(tree, monk1val)
    
    newPrunes = dtree.allPruned(tree)
    for prunedTree in newPrunes:
        if(goalCheck < dtree.check(prunedTree, monk1val)):
            myPrune(prunedTree)
    
    print "Check ", goalCheck
    print "TEST CHECK ", dtree.check(tree, m.monk1test)
    drawLib.drawTree(tree)

myPrune(decisionTree)

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
    



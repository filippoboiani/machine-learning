import monkdata as m 
import dtree as dtree
# uncomment if you want to import the draw class
#import drawtree_qt5 as drawLib

# assignment 4
# using select function in dtree to build the tree 
print "Select func doc: ", dtree.select.__doc__
print "Most common doc: ", dtree.mostCommon.__doc__
print "Check doc:       ", dtree.check.__doc__

bestAttribute = dtree.bestAttribute(m.monk1, m.attributes)
print "Best Attribute:  ", bestAttribute
dtree.select(m.monk1, bestAttribute, )

# assignment 5 
# build the decision tree and check the error for each dataset
decisionTree = dtree.buildTree(m.monk1, m.attributes)

# uncomment if you want to see the tree 
# drawLib.drawTree(decisionTree)
print "Decision Treee:\n  ", decisionTree
print "Check:   ", dtree.check(decisionTree, m.monk1test)
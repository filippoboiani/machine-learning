import monkdata as m 
import dtree as dtree
# uncomment if you want to import the draw class
import drawtree_qt5 as drawLib

# using select function in dtree to build the tree 
print "Select func doc: ", dtree.select.__doc__
print "Most common doc: ", dtree.mostCommon.__doc__
print "Check doc:       ", dtree.check.__doc__

print

# assignment 5 
# build the decision tree and check the error for each dataset
datasets = [{
        'name': 'monk1',
        'ref' : m.monk1,
        'test': m.monk1test
    },
    {
        'name': 'monk2',
        'ref' : m.monk2,
        'test': m.monk2test
    },
    {
        'name': 'monk3',
        'ref' : m.monk3,
        'test': m.monk3test
    }]

for dataset in datasets:
    print "Dataset:             ", dataset['name']
    decisionTree = None
    for maximumDepth in [2,5,10000]:
        decisionTree = dtree.buildTree(dataset['ref'], m.attributes, maximumDepth)
        print "Depth",maximumDepth
        print "   Check Training Set:  ", dtree.check(decisionTree, dataset['ref'])
        print "   Check Test Set:      ", dtree.check(decisionTree, dataset['test'])
        print "   Decision Treee:\n    ", decisionTree

    # uncomment if you want to see the tree or move to loop if you
    # want to see trees at all levels
    drawLib.drawTree(decisionTree)

# Below is a try to design naive implementation of dtree.buildTree
# using mostCommon, select and bestAttribute

# get the best attribute in terms of information gain
# split the dataset based on the values of the the selected attribute
# we will have as many branches as the attribute values.
# steps = []
# step = 0
# maxDepth = 2

# def split(subset, attribute, value):
#     print "Step:        ", step
#     print "Attribute:   ", attribute
#     print "Value:       ", value
#     step = step+1
#     bestAttribute = dtree.bestAttribute(subset, m.attributes)
#     for attr in m.attributes:
#         if attr.name == str(bestAttribute):
#             print "Decision node:   ", bestAttribute
#             for v in attr.values:
#                 split(subset, attr, v)

#     if step < 2:
#         split(subset, attr, v)

#     selection = dtree.select(subset, attribute, value)

# subset = m.monk1
# split(subset)

# for attribute in m.attributes:
#     values = attribute.values
#     for v in values:
#         subset = select(dataset, attribute, v)

# for attr in bestAttribute.value:
#     pass
# dtree.select(m.monk1, bestAttribute, )


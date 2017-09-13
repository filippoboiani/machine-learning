import monkdata as m 
import dtree as dtree

datasets = [{
        'name': 'monk1',
        'ref' : m.monk1
    },
    {
        'name': 'monk2',
        'ref' : m.monk2
    },
    {
        'name': 'monk3',
        'ref' : m.monk3
    }]



print "Sample class: " + m.Sample.__doc__


# TODO: 
# print dtree.averageGain(m.monk1, m.attributes)

for dataset in datasets:
    print "    Dataset: " + dataset['name']
    for attribute in m.attributes:
        print dtree.averageGain(dataset['ref'], attribute)
    

        
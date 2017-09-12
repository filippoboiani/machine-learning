import monkdata as m 
import dtree as dtree

print "Sample class: " + m.Sample.__doc__ 
print m.attributes

for sample in m.monk1:
    print sample.positive, sample.identity, " |||| ", sample.attribute

print "\n\n\n"
print "MONK 1       ", dtree.entropy(m.monk1)
print "MONK 2       ", dtree.entropy(m.monk2)
print "MONK 3       ", dtree.entropy(m.monk3)
print "MONK 1 TEST  ", dtree.entropy(m.monk1test)
print "MONK 2 TEST  ", dtree.entropy(m.monk2test)
print "MONK 3 TEST  ", dtree.entropy(m.monk3test)
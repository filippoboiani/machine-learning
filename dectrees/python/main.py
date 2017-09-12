import monkdata as m 

print "Sample class: " + m.Sample.__doc__ 
print m.attributes

import dtree as dt

# for monk in m.monk1:
#     print monk.attribute, monk.positive, monk.identity

print "Monk1", dt.entropy(m.monk1)
print "Monk2", dt.entropy(m.monk2)
print "Monk3", dt.entropy(m.monk3)
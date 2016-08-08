list = [u'%MEM %CPU\n', u'32.3  0.7\n']
list1 = list[0]
x= list1.split()
list2 = list[1].replace('  ',' ')
y= list2.split()

#print x
#print y

for i in range(1):
    (q,w) = (x[i],y[i])
    prac = (q,w)
    d1= dict([prac])

print d1

for i in range(2):
    (q,w) = (x[i],y[i])
    prac = (q,w)
    d2= dict([prac])

print d2

d3 = dict(d1,**d2)
print d3


#my_dict = {"test": 1, "testing": 2}

with open('test10.csv', 'a') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, d3.values())
    w.writeheader()
    w.writerow(d3)

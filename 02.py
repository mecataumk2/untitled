tuple = (1, 2)
list = [1, 2]
dict = {
    'name':'Seungdae Lee',
    'age':'20'
}

x, y = tuple

print "Start out"
print tuple
print x
print y
print dict

with open('sample.txt', 'rt') as f:
    data = f.read()
    print data

if False:
    print 'hello 1'
print 'hello 2'

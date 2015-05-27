file_test = open('sample.txt', 'rt') 

 
print type(file_test)
print file_test

lines = file_test.readlines()

print type(lines)
print lines[1: 3]
print len(lines[1:2])

range_1 = range(100, 105)
print type(range_1)
print range_1

 
for number in range_1:
    print number

 
for line in lines:
    print line

#print type(line)

#if isinstance(line, str) and '@' in str
#    print line



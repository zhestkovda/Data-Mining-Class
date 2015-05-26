import sys

filename =sys.argv[1]
f = open(filename)
fo = open('output.svc', 'w')


line = f.readline()
while (len(line)>0):
    
    ids = line.split()


    for id in ids:
        fo.write(id+'\n')
    line = f.readline()
f.close()
print 'Completed'

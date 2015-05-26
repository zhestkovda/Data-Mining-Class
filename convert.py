import sys

filename =sys.argv[1]
f = open(filename)
f_nodes = open('nodes.csv', 'w')
f_edges = open('edges.csv','w')

line = f.readline()
while (len(line)>0):
    
    someone = line.split()
    i=someone[0]
    print i
    followers = ' '.join(someone[1:])
    f_nodes(i+'\n')
    f_edges(followers+'\n')
    line = f.readline()

f.close()
print 'Completed'

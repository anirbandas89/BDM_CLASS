import numpy as np

data = np.loadtxt('BBN_full_Parthenelope_880.3.dat')

f = open('BBN_full_Parthenelope_880.3_class_format.dat', 'w')
#print data[0]

for i in range(len(data)):
    f.write(str(data[i,0])+'  ')
    f.write(str(data[i,2])+'  ')
    f.write(str(data[i,3])+'\n')

print len(data)
#f.write( str(data[0,0])+'  '  )
#f.write(str(data[0,2])+'  ')
#f.write(str(data[0,3])+'\n')
#f.write(str(data[1,0]))
f.close()

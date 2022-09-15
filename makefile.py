import os
filename = 'aloha.txt'
f = open(filename,'w')
f.write("makelife")
f.close()
f = open('aloha.txt','r')
print(f.read())

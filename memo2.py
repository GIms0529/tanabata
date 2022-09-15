import os
filename = 'memo.txt'
f = open(filename, 'w')
memo = input('input memo> ')
f.write(memo)
f.close()
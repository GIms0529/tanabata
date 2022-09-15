import os
filename = 'memo.txt'
f = open(filename,'w')
memo = 'ALOHA！\n僕たちはIG12クラスです。\nよろしく。\n'
f.write(memo)
f.close()
rows = 12
columns = 12
routs = [[0 for x in range(1, columns)] for x in range(1,rows)]
for i in range(1,rows-1):
    for j in range(1, columns-1):
        routs[i][j] = '%s,%s'%(i,j)
print(routs)
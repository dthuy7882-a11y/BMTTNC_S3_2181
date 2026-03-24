input_str = input("Nhap X, Y: ")
dimnesions=[int(x) for x in input_str.split(',')]
rowNum=dimnesions[0]
colNum=dimnesions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)
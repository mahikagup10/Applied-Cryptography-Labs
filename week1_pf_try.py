matrix = [[],[],[],[],[]]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
key = "WORK"

added = []
row = 0
col = 0

for i in key:
    if i not in added:
        matrix[row].append(i)
        added.append(i)
    if col==4:
        col = 0
        row = row+1
    else:
        col = col+1

for i in letters:
    if i not in added:
        added.append(i)

for i in range(5):
    for j in range(5):
        matrix[i].append(added[i])

print(matrix)
    

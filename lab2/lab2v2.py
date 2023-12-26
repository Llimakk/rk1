#        e d i t i n g
#   0  0 1 2 3 4 5 6 7
#      _______________
#   0| 0 1 2 3 4 5 6 7
# d 1| 1 1 1 2 3 4 5 6
# i 2| 2 2 2 1 2 3 4 5
# s 3| 3 3 3 2 2 3 4 5
# t 4| 4 4 4 3 2 3 4 5
# a 5| 5 5 5 4 3 3 4 5
# n 6| 6 6 6 5 4 4 3 4
# c 7| 7 7 7 6 5 5 4 4
# e 8| 8 7 8 7 6 6 5 5

print("Введите первое слово:")
w1 = input()
print("Введите второе слово:")
w2 = input()
len1 = len(w1)+1
len2 = len(w2)+1
matrix = [[0]*len1 for i in range (len2)]
for i in range(0, len1):
    matrix[0][i] = i
for j in range(0, len2):
    matrix[j][0] = j
for i in range(0,len1-1):
    for j in range(0,len2-1):
        if w1[i] != w2[j]:
            matrix[j+1][i+1] = min(matrix[j][i+1],matrix[j][i],matrix[j+1][i]) + 1
        elif w1[i] == w2[j]:
            matrix[j+1][i+1] = min(matrix[j][i+1],matrix[j][i],matrix[j+1][i])
print('Расстояние Левенштейна =',matrix[len2-1][len1-1])

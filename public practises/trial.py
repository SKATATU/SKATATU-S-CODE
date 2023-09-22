from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

for i in range(0,15):
    T.replace(" ","")
    if len(str(T[i][i])) == 1:
            T[i][i] = '%02d' % T[i][i]
    elif len(str(T[i][i])) != 1:
            T[i][i] = T[i][i]
txt1 = str(T[0])
txt1 = txt1.replace("[","") 
txt1 = txt1.replace("]","")
txt1 = txt1.replace(",","|")
txt1 = txt1.replace(" ","")
print(txt1)

txt2 = ""
for i in range(0,len(T)):
    txt2 = txt2 + str(T[i][0]) + " "

txt2 = txt2.replace("[","")
txt2 = txt2.replace("]","")
txt2 = txt2.replace(" ","|")
txt2 = txt2[:len(txt2)-1]
print(txt2)



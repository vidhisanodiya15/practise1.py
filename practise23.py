#write a python program to print duplicates present in  list.
l =["hello",10,20,40,60,20,40,30]
d=[]
for ele in l :
    if l.count(ele)>1:
            d.append(ele)
print(d)


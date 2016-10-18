import statistics

#read txt, put into list.
a = open('google.txt', 'r')
Lines1 = a.readlines()
a.close()
new1 = []                               
for line in Lines1:
    temp1 = line.strip('\n')     
    temp2 = temp1.split(',')
    new1.append(temp2)

b = open('bing.txt', 'r')
Lines2 = b.readlines()
b.close()
new2 = []                               
for line in Lines2:
    temp3 = line.strip('\n')     
    temp4 = temp3.split(',')
    new2.append(temp4)

c = open('yahoo.txt', 'r')
Lines3 = c.readlines()
c.close()
new3 = []                               
for line in Lines3:
    temp5 = line.strip('\n')     
    temp6 = temp5.split(',')
    new3.append(temp6)
    

#find index for list

#12
find1=['  12. http://www.google.com/webhp?hl=']
print("Index for 'http://www.google.com/webhp?hl=': ", new1.index(find1))

#14
find2=['  13. https://www.python.org/']
print("Index for 'https://www.python.org/': ", new2.index(find2))

#7
find3=['  13. https://mobile.yahoo.com/;_ylt=A0LEVyAh1_5XBscAtN5XNyoA']
print("Index for 'https://mobile.yahoo.com/;_ylt=A0LEVyAh1_5XBscAtN5XNyoA': ", new3.index(find3))


#ranking list
list1=[]
list2=[]
list3=[]

# a<b<c
if new1.index(find1) < new2.index(find2) < new3.index(find3):
        list1.append(2)
        list2.append(1)
        list3.append(0)
        
# a<c<b        
if new1.index(find1) < new3.index(find3) < new2.index(find2):
        list1.append(2)
        list2.append(0)
        list3.append(1)

# a=b<c
if new1.index(find1) == new2.index(find2) < new3.index(find3):
        list1.append(2)
        list2.append(2)
        list3.append(0)

# a=c<b
if new1.index(find1) == new3.index(find3) < new2.index(find2):
        list1.append(2)
        list2.append(0)
        list3.append(2)

# a<b=c
if new1.index(find1) < new2.index(find2) == new3.index(find3):
        list1.append(2)
        list2.append(1)
        list3.append(1)

# b<a<c
if new2.index(find2) < new1.index(find1) < new3.index(find3):
        list1.append(1)
        list2.append(2)
        list3.append(0)

# b<c<a
if new2.index(find2) < new3.index(find3) < new1.index(find1):
        list1.append(0)
        list2.append(2)
        list3.append(1)

# b=c<a
if new2.index(find2) == new3.index(find3) < new1.index(find1):
        list1.append(0)
        list2.append(2)
        list3.append(2)

# b<a=c
if new2.index(find2) < new1.index(find1) == new3.index(find3):
        list1.append(1)
        list2.append(2)
        list3.append(1)

# c<b<a
if new3.index(find3) < new2.index(find2) < new1.index(find1):
        list1.append(0)
        list2.append(1)
        list3.append(2)

# c<a<b
if new3.index(find3) < new1.index(find1) < new2.index(find2):
        list1.append(1)
        list2.append(0)
        list3.append(2)

# c<b=a
if new3.index(find3) < new2.index(find2) == new1.index(find1):
        list1.append(1)
        list2.append(1)
        list3.append(2)

# a=b=c
if new1.index(find1) == new2.index(find2) == new3.index(find3):
        list1.append(2)
        list2.append(2)
        list3.append(2)

print("point for list1: ", list1)
print("point for list2: ", list2)
print("point for list3: ", list3)

#get mean for list
mean1=sum(list1)/len(list1)
mean2=sum(list2)/len(list2)
mean2=sum(list3)/len(list3)

statistics.median(list1)
statistics.median(list2)
statistics.median(list3)



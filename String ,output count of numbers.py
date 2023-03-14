
'''we have a string  s = "12223311", output should be 11233212 .
which means in s , 1 occurs 1 time , then 2 occurs 3 times , then 3 occurs 2 times and
then 1 occurs 2 times so output is 11233212. Program using python
'''

s = "12223311"

#11233212
str1=""
prev =None
count=0

for c in s:
    if c==prev: #2==1,no #2==2yes #2==2yes #3!=2 #3==3 #1!=3
        count+=1 #2 #3 , #2
    else:
        if prev:
            print(prev+str(count),end="") #11 #23 #32
        prev =c #1 #2 #3 #1
        count=1 #1 #1 #1

if prev:
     print(prev + str(count),end="")

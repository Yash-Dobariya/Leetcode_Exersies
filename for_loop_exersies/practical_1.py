"""Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
 between 1500 and 2700 (both included). """
stat_len=1500
stop_len=2700

list1=[]

for i in range(stat_len,stop_len+1):
    if i % 7 == 0 and i % 5 == 0:
        list1.append(str(i))
print(','.join(list1))
        

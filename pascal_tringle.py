user_input=5

for i in range(1,user_input+1):

    for j  in range(i-1,user_input-1):
        print(" ",end=' ')
    m=1
    for j in range(i,i*2):
        print(m, end = " ")
        m = int(m * (i - j) / j) 
     
    print("\n")
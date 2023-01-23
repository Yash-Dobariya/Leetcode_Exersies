user_input=int(input("Enter your row: "))
count=1

for row in range(1,user_input+1):

    for col in range(row-1,user_input-1):
        print(" ",end='')

    for col in range(row):
        if  col == 0 :
            count=1
        else: 
          count=count*(row-col)//col
        print(count,end=' ')
    print()
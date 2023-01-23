user_input=int(input("Enter your number : "))

for i in range(0,user_input+1):
    for j in range(1,i+1):
        print("*",end=" ")     
    # print(" ")

for i in range(0,user_input+1): 
    for j in range(i-1,user_input):
        print("*",end=" ")
        
    print()
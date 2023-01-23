list1=['man','van','bee','dumble']

str1=str(list1)
result = dict()
for i in list1:
    for j in i:
        if j in result:
            result[j]+=1
        else:
            result[j]=1


print(result)
# user_input=input("Enter your str : ")

# for i in str1:
#     count_str=str1.count(user_input)
#     print(count_str,end='')
#     break


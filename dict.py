data = "yash_dobariya"
data_dict = dict()

for i in data:
    if i in data_dict:
        data_dict[i]+=1
    else:
        data_dict[i]=1
print(data_dict)
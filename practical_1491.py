# 1491. Average Salary Excluding the Minimum and Maximum Salary
salary = [1000, 2000, 3000]

"""First Method"""

# minimum=min(salary)
# maximum=max(salary)
# avg= (minimum + maximum)/2
# print(avg)

"""Secound Method"""

lenth = len(salary)
min_salary = salary[0]
max_salary = salary[0]

for i in range(lenth):

    if min_salary > salary[i]:
        min_salary=salary[i]

    if max_salary < salary[i]:
         max_salary=salary[i]

avg = (min_salary + max_salary) / 2
print(avg)
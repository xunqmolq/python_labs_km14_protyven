salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
after_list = []
sum_of_index = []
print (" Salary table: ")
for i in salary_list:
    a = i*1.3
    b = i*0.3
    after_list.append (round(a,2))
    sum_of_index.append (round(b,2))
print ("First salary value: ", *salary_list)
print ("Salary value after indexing: ", *after_list)
print ("sum of indexation: ", *sum_of_index)

    
    
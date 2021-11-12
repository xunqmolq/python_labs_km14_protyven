salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
print ("Salary table:\n", "Before indexation:", salary_list)
def index(i):
    return round(i*1.3,2)
salary_ind = list(map(index, salary_list))
print ("After indexation:", salary_ind)
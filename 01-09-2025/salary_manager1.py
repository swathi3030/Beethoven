salaries=[]
#CRUD- CREATE,READALL, READ BY ID, UPDATE, DELETE

def create_salary(salary):
    global salaries
    salaries.append(salary)

def read_all():
    return salaries

def read_by_salary(salary):
    for I in range(len(salaries)): 
        if salaries[I] == salary:
            return I
    return -1

def update(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index]= new_salary

def delete_by_salary(salary):
    global salaries
    index = read_by_salary(salary)
    salaries.pop(index)

create_salary(1000)
create_salary(2000)
create_salary(8000)
create_salary(3000)
arr=read_all()
for salary in arr:
    print(salary)
print(read_by_salary(8000))
print(read_by_salary(4000))
print(salaries[read_by_salary(8000)])

update(8000,8500)
print(read_all())

delete_by_salary(1000)
print(read_all())
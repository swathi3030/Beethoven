from salary_manager import create_salary, read_all, read_by_salary, salaries,update, delete_by_salary
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
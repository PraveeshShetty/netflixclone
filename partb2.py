emp_array=[]
class Employee:
    def __init__(self,empno,name,depname,des,age,sal):
        self.empno=empno
        self.name=name
        self.depname=depname
        self.des=des
        self.age=age
        self.sal=sal
n=int(input("enter no of employees:"))
for i in range(n):
    en=int(input("enter employee no:"))
    na=input("enter name:")
    dname=input("enter department name:")
    de=input("enter designation:")
    ag=int(input("enter employee age:"))
    salary=int(input("enter employee salary:"))
    emp_array.append(Employee(en,na,dname,de,ag,salary))
for i in range(0,len(emp_array)):
    print("\nempno:",emp_array[i].empno,
          "\nempname:",emp_array[i].name,
          "\ndeptname:",emp_array[i].depname,
          "\ndesignation:",emp_array[i].des,
          "\nage:",emp_array[i].age,
          "\nsalary:",emp_array[i].sal)
item=int(input("enter searching employee number"))
for i in range(0,len(emp_array)):
    if(item==emp_array[i].empno):
        print("searching employee found")
        print("\nempno:",emp_array[i].empno,
          "\nempname:",emp_array[i].name,
          "\ndeptname:",emp_array[i].depname,
          "\ndesignation:",emp_array[i].des,
          "\nage:",emp_array[i].age,
          "\nsalary:",emp_array[i].sal)
        break
else:
    print("searching employee not found")
    
    

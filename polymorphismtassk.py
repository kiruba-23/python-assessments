class Employee:
    def calculate_salary(self):
        print("Total salary")

class permanent_employee(Employee):
    def calculate_salary(self):
       print("Only for permanent employee")
       print("____________________________")
       self. basicsalary=int(input("Enter your basic salary: "))
       self.bonous=int(1000)
       self.totalsalary=self.basicsalary+self.bonous
       print("permanent Employee salary:",self.totalsalary)
       return self.totalsalary

class contract_employee(Employee):
    def calculate_salary(self):
        print("Only for conctract employee")
        print("_____________________________")
        self.onehour=int(300)
        self.workinghours=int(input("Enter your working hours:"))
        self.totalsalary=self.workinghours*self.onehour
        print("contract_employee salary:",self.totalsalary)
        return self.totalsalary

class intern(Employee):
    def calculate_salary(self):
        print("Only for intern employee")
        print("__________________________")
        self.dailystipend=int(900)
        self.workingdays=int(input("Enter your working days:"))
        self.totalsalary=self.dailystipend*self.workingdays
        print("intern employee salary:",self.totalsalary)
        return self.totalsalary

object1=permanent_employee()
print(object1.calculate_salary())
object2=contract_employee()
print(object2.calculate_salary())
object3=intern()
print(object3.calculate_salary())
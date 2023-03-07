# exec(open(r"D:\Class\Code_files\Practice\Django_practice\EmpProject\app1\db_shell.py").read())

from app1.models import *

# e1 = Employee.objects.all()
# print(e1)


# e1 = Employee(name="Yash Bhosarkar", age=27, salary=67000, address="Satara")
# # print(e1)
# e1.save()

# Employee.objects.create(name="Yash Bhosarkar", age=27, salary=67000, address="Satara")



# e1 = Employee.objects.all()
# print(e1)

# e1 = Employee.objects.get(id=3)
# # print(e1.__dict__)

# e1 = Employee.objects.filter(id__lte=2)
# e1 = Employee.objects.filter(name__startswith='M')
# e1 = Employee.objects.filter(name__endswith='r')
# e1 = Employee.objects.filter(name__contains='M')
# print(dir(e1))

# e1.name = 'Mayur Totare'
# e1.address = 'Pune'

# e1.save()

# e1.delete()

# e1 = Employee.objects.select_related()
# e1 = Employee.objects.prefetch_related()
# print(e1)


# Employee.objects.bulk_create([Employee(name="Uddhav Thakare", age=55, salary=67000, address="Mumbai"),
#                                 Employee(name="Sharad Pawar", age=87, salary=67000, address="Baramati"),
#                                 Employee(name="Narendra Modi", age=67, salary=67000, address="Gujrat")
#                             ])


# e1 = Employee.objects.get(id = 5)
# for i in e1:
# print(e1.__dict__)
# e1.is_active = True
# e1.save()


# e1 = Employee()

# data = Employee.active_data()
# iter_obj = iter(data)

# t1 = next(iter_obj)
# t1.is_active = False
# t1.save()

# print(next(iter_obj))

# inactive = e1.inactive_data()
# print(inactive)


# comp = Company.objects.get(id=1)

# print(comp.prod.all())


# man = Manager.objects.get(name__startswith='1')
# print(man.company)


# emp = Employee.objects.get(id = 1)
# print(emp.company)


# custm = Customer.objects.get(id= 1)

# single_product = custm.product.get(name='TV')
# print(custm.product.all()[0].company)
# print(single_product.company)

# comp = Company.objects.get(id=1)
# print(comp.prod.all()[0].cust.all())
# print(dir(comp.prod.all()[0]))

# -------------------------------------- 

# comp = Company.objects.get(id=4)
# print(comp.manager)
# comp.manager.delete()

# for i in comp:
#     print(i.manager)


# Company.objects.create(name='Accenture pvt.ltd', place='Kolkata')

# comp.manager = Manager(name='Umesh Yadav', salary=75000)
# comp.manager.save()

# Manager.objects.create(name='Umesh Yadav', salary=75000, company_id=4)


# emps = Employee.objects.select_related().all()   #-- select related
# for emp in emps:
#     print(emp.company)


# comp = Company.objects.prefetch_related('emp').all()  #-- prefetch related

# for i in comp:
#     print(i.emp.all())

# from django.contrib.auth.models import User

# user = User.objects.get(id=3)

# print((user.profile.bio))


# user = User.objects.get(id=5)
# user.delete()

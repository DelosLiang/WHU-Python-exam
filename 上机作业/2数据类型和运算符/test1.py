import datetime
sName=str(input("请输入您的姓名："))
s=int(input("请输入您的出生年份："))
age=datetime.date.today().year-s
print("您好！{0}。您{1}岁。".format(sName,age))

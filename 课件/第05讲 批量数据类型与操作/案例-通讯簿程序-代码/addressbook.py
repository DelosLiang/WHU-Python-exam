"""简易通讯簿程序"""
import os, json

ab = {} #通讯簿保存在字典中name:tel

#从JSON文件中读取通讯簿
if os.path.exists("addressbook.json"):
    with open(r'addressbook.json', 'r', encoding='utf-8') as f:
        ab = json.load(f)
		
while True:  
    print("|---欢迎使用通讯簿程序---|")  
    print("|---1：显示通讯簿清单 ---|")  
    print("|---2：查询联系人资料 ---|")  
    print("|---3：插入新的联系人 ---|")  
    print("|---4：删除已有联系人 ---|")  
    print("|---0：退出 -------------|")
    choice = input('请选择功能菜单(0-4):')
	
    if choice == '1':  # 1：显示通讯簿清单 
        if(len(ab)==0):
            print("通讯簿为空")
        else:
            for k, v in ab.items():
                print("姓名={},联系电话={}".format(k, v))
				
    elif choice == '2':  # 2：查询联系人资料
        name = input("请输入联系人姓名：")
        if(name not in ab):
            ask = input("联系人不存在，是否增加用户资料(Y/N)")  
            if ask in ["Y", "y"]:  
                tel = input("请输入用户联系电话：")  
                ab[name] = tel
        else:
            print("联系人信息：{} {}".format(name, ab[name]))
			
    elif choice == '3':  # 3：插入新的联系人
        name=input("请输入联系人姓名：")  
        if(name in ab):  
            print("已存在联系人：{} {}".format(name, ab[name]))  
            ask = input("是否修改用户资料(Y/N)")  
            if ask in ["Y", "y"]:  
                tel = input("请输入用户联系电话：")  
                dict[name] = tel  
        else:  
            tel = input("请输入用户联系电话：")  
            ab[name] = tel                  
			
    elif choice == '4':  # 4：删除已有联系人
        name = input("请输入联系人姓名：")
        if(name not in ab):  
            print("联系人不存在：{}".format(name))
        else:
            tel = ab.pop(name)
            print("删除联系人：{} {}".format(name, tel))
			
    elif choice == '0': # 保存到JSON文件并退出循环
        with open(r'addressbook.json', 'w', encoding='utf-8') as f:
            json.dump(ab, f)        
        break

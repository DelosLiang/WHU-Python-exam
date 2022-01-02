# hello.py
from flask import Flask
app = Flask(__name__)		# 创建Flask对象

@app.route('/')				# 通过装饰器定义请求URL目录“/”的操作
def hello_flask():			# 定义函数对URL目录“/”请求进行处理
    return '<h1><b>Hello, Flask!</b></h1>'	# 返回字符串（网页的HTML代码）
	
if __name__=='__main__':
    app.run()				# 运行应用程序
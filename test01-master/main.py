#czj Data 2020.04.11
import flask, os, sys,time
from flask import request,render_template,Flask, url_for, request, json,jsonify

interface_path = os.path.dirname(__file__)#os.path.dirname(__file__)为当前文件的绝对路径
sys.path.insert(0, interface_path)  #将当前文件的父目录加入临时系统变量

server = flask.Flask(__name__, static_folder='static')#默认的静态文件的位置是在 static目录下，故图片默认存储在该目录文件中

@server.route('/', methods=['get','post']) #设置路由
def index():
   # win32api.ShellExecute(0,'open','C:\\Users\\86187\\Desktop\\test01-master\\my_deepsort.py','','',1)
   #


    #os.system('python my_deepsort.py')
    return render_template("index.html") #不带参跳转页面

@server.route('/upload', methods=['get','post']) #设置路由
def upload():
    fname = request.files['img']  #获取上传的文件
    if fname:
        t = time.strftime('%Y'+'Y'+'%m'+'M'+'%d'+'D'+'%H%M%S')#获取当前时间
        new_fname = r'static/photo/' + t + fname.filename  #文件保存路径
        print("保存视频到指定路径...")
        fname.save(new_fname)  #保存文件到指定路径python my_deepsort.py --VIDEO_PATH video-01.avi
        print("正在读入目标视频...")
        with os.popen('python my_deepsort.py --VIDEO_PATH %s' %new_fname, "r") as p:
            r = p.read()
        print(r+"\n"+"成功读取目标视频！"+"\n"+"目标视频存储路径:"+new_fname)
        return '<img src=%s>' %  new_fname
    else:
        return '{"msg": "请上传文件！"}'

print('----------路由和视图函数的对应关系----------')
print(server.url_map) #打印路由和视图函数的对应关系
server.run(port=8000)

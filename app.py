from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    print("Hello, World!")
    return "<p>Hello, World!</p>"

@app.route("/classinfo/<order>")
def get_class_order(order):
    print(order)
    return {
        "id": "11110A",
        "name": "高等数学",
        "teacher": "张三",
        "time": ["周一 1-2节", "周三 3-4节"],
        "rate": 4.5,
        "location": "教学楼A101",
    }
    
@app.route("/userinfo/<order>")
def get_user_order(order):
    print(order)
    return {
        "id": "J221525",
        "name": "胥昱泉",
        "avatar": "https://files.lsmcloud.top/blog26111653219843_.jpg"
    }
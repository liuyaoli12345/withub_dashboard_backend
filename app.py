from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    print("Hello, World!")
    return "<p>Hello, World!</p>"

@app.route("/class/<order>")
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
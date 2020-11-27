from flask import Flask,render_template,request
app =  Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def index():
    return render_template("index.html",message="Helohelo!")

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/result',methods="GET")
def result():
    get_input=request.args.get("query","")
    print(get_input)
    return 'Hello, World!'

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=8888)
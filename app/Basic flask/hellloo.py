from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route('/hi/<name>')
def hello_name(name):
    return "Hello %s!" %name

@app.route('/Integer/<int:number>')
def hello_std(number):
    return "Standard %d!" %number

@app.route('/Float/<float:pointer>')
def hello_pointer(pointer):
    return "Pointer %f!" %pointer


if __name__=='__main__':
    app.run(debug=True)
    

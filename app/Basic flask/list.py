from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    
    li

    st=["sajal","shrita","jinal"]
    dict={"name":"Sajal","age":20,"gender":"female"}
    tuple=({"name":"Sajal","age":20})
    return render_template('result.html', list=list,dict=dict,tuple=tuple)
    


if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/index')
def index():
    user={"username":"Dhiraj"}
    posts=[
        {"author" : {"username":"Daniel"},
         "body":"Beautiful day in srilanka"
         },
        {"author" : {"username":"Amar"},
         "body":"Tiger Zinda Hai movie was so cool"
         }
        ]
    return render_template('activity.html',user=user,posts=posts)
            
    
if __name__=='__main__':
    app.run(debug=True)
    

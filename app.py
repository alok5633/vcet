from flask import Flask,request,jsonify,render_template
import json

app=Flask(__name__)

 

@app.route('/',methods=['GET','POST'])
def home():
    
    if request.method == "POST":
        text = request.args.post('jsdata')
        print(text)
    else:    
       return render_template('index.html')
    
    
    
if __name__ == '__main__':
    app.run()    
    


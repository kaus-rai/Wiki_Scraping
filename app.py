import os
from flask import Flask, render_template, request
import Wiki_Info
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/details', methods=['GET','POST'])
def schedule():
    college=request.form.get('url_to_search')
    items=Wiki_Info.scraper(college)
    return render_template('details.html',content=items)
    
        
if __name__ == '__main__':
    host=os.environ.get('IP','127.0.0.1')
    port= int(os.environ.get('PORT', 5000))
    app.run(host=host,port=port)

from flask import Flask
from flask import render_template, request
from dummy import printme
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    q=request.args.get('query')
    
    if q:
        a=printme(q) #dummy function - printme from a dummy.py file, these values will be passed on to the search html
        return render_template('search.html',q=q, dummy=a)

    return render_template('index.html')



@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
   app.run(debug = True)
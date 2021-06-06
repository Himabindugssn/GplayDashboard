from flask import Flask
from flask import render_template, request,jsonify
from search import Search
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    q=request.args.get('query')
    
    if q:
        data=Search(q)
        # data=jsonify(HTMLTab=data)
        return render_template('search.html',q=q, data=data)

    return render_template('index.html')



@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
   app.run(debug = True)
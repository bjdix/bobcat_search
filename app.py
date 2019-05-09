from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from elasticsearch import Elasticsearch

application = app = Flask(__name__)
bootstrap = Bootstrap(app)
es = Elasticsearch()

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		selectedValue = request.form['options']
		print (selectedValue)
		return redirect(url_for('click', selectedValue=selectedValue))
	return render_template('base.html')

@app.route('/<selectedValue>',  methods=['GET', 'POST'])
def click(selectedValue):
	if request.method == 'POST':
		selectedValue = request.form['options']
		print (selectedValue)
		return redirect(url_for('click', selectedValue=selectedValue))
	return render_template(selectedValue + '.html', buttons=['websearch','localsearch'], active_btns=['selectedValue'])

@app.route('/ls', methods=['GET','POST'])
def local_search():
	q = request.form.get('q')
	if q is not None:
		payload = {
		    "query": {
		        "query_string": {
		            "analyze_wildcard": True,
		            "query": str(q),
		            "fields": ["song", "artist", "rank", "year","lyrics"]
		        }
		    },
		     "highlight" : {
        		"fields" : {
        			"song" : {},
        			"artist" : {},
        			"year" : {},
        			"rank" : {},
        			"lyrics": {}
        		}
    		},
		    "size": 50,
		    "sort": [

		    ]
		}
		print("!!!!!!!!!!!!!")
		resp = es.search(index='lyrics', body=payload)
		print("??????????????")
		return render_template("localsearch.html", q=q, response=resp)
	else:
		selectedValue = request.form['options']
		return redirect(url_for('click', selectedValue=selectedValue))

if __name__ == '__main__':
    app.run("0.0.0.0",port=8005,debug=False,threaded=True)
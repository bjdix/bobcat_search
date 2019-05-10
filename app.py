from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from flask_bootstrap import Bootstrap
import os
import requests,json

application = app = Flask(__name__)
bootstrap = Bootstrap(app)


headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		selectedValue = request.form['options']
		return redirect(url_for('click', selectedValue=selectedValue))
	return render_template('base.html')

@app.route('/<selectedValue>',  methods=['GET', 'POST'])
def click(selectedValue):
	if request.method == 'POST':
		selectedValue = request.form['options']
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
		payload = json.dumps(payload)
		url = "http://elasticsearch:9200/_search"
		response = requests.request("GET", url, data=payload, headers=headers)
		response_dict_data = json.loads(str(response.text))
		return render_template("localsearch.html", q=q, response=response_dict_data)
	else:
		selectedValue = request.form['options']
		return redirect(url_for('click', selectedValue=selectedValue))

if __name__ == '__main__':
    app.run("0.0.0.0",port=8005,debug=False,threaded=True)
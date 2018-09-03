from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def main(query=1):
	
	if query.isdigit():
		r = requests.get('http://pokeapi.co/api/v2/pokemon/' + query)
		data = r.json()
		query = "The pokemon with id " + query + " is " + data["name"]

	else:
		r = requests.get('http://pokeapi.co/api/v2/pokemon/' + query)
		data = r.json()
		query = query + " has id " + str(data["id"])
	return render_template('index.html', query=query)


if __name__ == '__main__':
    app.run()

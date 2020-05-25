from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/moi')
def moi_meme():
	return 'Salue Mr Gawonou'


@app.route('/hello/<nom>')
def hello_world(nom):
	return 'Hello  %s!' % nom


@app.route('/python')
def Python_test():
	return 'Hello  python'

"""@app.route('/hello/<name>')
def hello():
	if name == moi:
		return redirect(url_for('moi'))
	else:
		return redirect(url_for('hello_world', nom = name))
"""

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nom']
		return redirect(url_for('hello_world', nom = user))
	else:
		user = request.args.get('nom')
		return redirect(url_for('hello_world', nom = user))



if __name__ == '__main__':
	app.debug = True
	app.run(debug = True)
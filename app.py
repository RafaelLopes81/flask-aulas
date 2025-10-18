from flask import Flask, render_template, request, redirect, url_for

class Myapp:

	def __init__(self):
		self.app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
		self.app.add_url_rule('/', 'index', self.index)
		self.app.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])

	def index(self):
		return render_template('index.html', title='Home Page')

	def login(self):
		if request.method == 'POST':
			email = request.form.get('email')
			password = request.form.get('password')	
			
			if not email or not password:
				return render_template('login.html', title='Login Page', error='Email ou senha não podem estar vazios.')
			return redirect(url_for('index'))
		return render_template('login.html', title='Login Page')
	

	def run(self):
		self.app.run(debug=True)

	

if __name__ == '__main__':
    my_app = Myapp()
    my_app.run()    
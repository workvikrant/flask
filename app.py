from flask import Flask , render_template

app = Flask(__name__)
#  app.secret.key nessarry

@app.route('/')
def index():
    return render_template('home.html')

app.run (debug=True, host='0.0.0.0' , port=5000)

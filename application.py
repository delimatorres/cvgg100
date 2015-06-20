from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')
   
if __name__ == '__main__':
    app.run()
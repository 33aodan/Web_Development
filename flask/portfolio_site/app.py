from flask import render_template, Flask, request  

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/finish')
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)
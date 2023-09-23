from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
messages=[""]
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    messages.append({"name": name, "email": email, "message": message})

    return redirect(url_for("Thank_you"))

@app.route('/Thank_you')
def Thank_you():
    return "Thank you for contacting us"
if __name__ == '__main__':
    app.run()
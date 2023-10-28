from flask import Flask, request, render_template
#flask is used to make a new flask app
#request is used to get or post something on an application
#render templaer renders an html page on a particular url

#making flask app
app = Flask(__name__)

quiz_question = "what is the best hero in clash of clans?"
quiz_option = ["Barbarian King", "Warden", "Royal Champion", "Queen Archer"]
correct_answer = "Queen Archer"
@app.route('/')
def index():
    return "welcome to the quiz application"

@app.route('/quiz', methods=['GET','POST'])
def quiz():
    if request.method == "POST":
        user_answer = request.form.get('answer')
        if user_answer == correct_answer:
            return "Correct! Queen Archer is the best hero in clash of clans."
        else:
            return "Incorrect! Try again."
    return render_template('quiz.html', question=quiz_question, options=quiz_option)

if __name__ =="__main__":
    app.run(debug=True)
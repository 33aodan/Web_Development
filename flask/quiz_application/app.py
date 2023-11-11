from flask import Flask, request, render_template
#flask is used to make a new flask app
#request is used to get or post something on an application
#render templaer renders an html page on a particular url

#making flask app
app = Flask(__name__)

questions = [
    {
        "question" : "what is the place where ethan lives",
        "options" : ["london", "new mexico", "houston", "chicago"],
        "correct_answer" : "new mexico"
    },
    {
        "question" : "what is the place where baodan lives",
        "options" : ["london", "new mexico", "houston", "chicago"],
        "correct_answer" : "chicago"
    },
    {
        "question" : "what is the place where queen lives",
        "options" : ["london", "new mexico", "houston", "chicago"],
        "correct_answer" : "london"
    }
]

leaderboard_list=[
    {'username' : 'Baodan', 'score' : 69},
    {'username' : 'Ethan', 'score' : 42},
    {'username' : 'Celina', 'score' : 90},
    {'username' : 'Angelina', 'score' : 50}
]

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', leaderboard=leaderboard_list)
score = 0
current_question = 0

@app.route('/')
def index():
    return "welcome to the quiz application"

@app.route('/quiz', methods=['GET','POST'])
def quiz():
    global score
    global current_question
    if request.method == "POST":
        user_answer = request.form.get('answer')
        correct_answer = questions[current_question]["correct_answer"]
        if user_answer == correct_answer:
            score += 1
        current_question += 1
        if current_question < len(questions):
            return render_template("quiz.html", question = questions[current_question]["question"], options=questions[current_question]["options"])
        else:
            feedback = f"You scored {score}/{len(questions)}.)"
            score = 0
            current_question = 0
            return render_template("result.html", feedback=feedback)
    return render_template("quiz.html", question = questions[current_question]["question"], options=questions[current_question]["options"])

if __name__ =="__main__":
    app.run(debug=True)
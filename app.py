from flask import Flask

app = Flask(__name__)


@app.route('/createQuiz')
def createQuiz():
    # Process the request data and convert to a note object
    # Create quiz question from note object
    # Return the quiz question
    pass


@app.route('/checkAnswer')
def checkAnswer():
    pass


if __name__ == '__main__':
    app.run()

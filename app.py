from flask import Flask
from config import Config

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

@app.route('/')
def checkConfig():
    print('ENV:      {}'.format(Config.ENV))
    print('COHERE_API_KEY:  {}'.format(Config.COHERE_API_KEY))
    print('HOSTNAME: {}'.format(Config.HOSTNAME))
    print('PORT:     {}'.format(Config.PORT))


if __name__ == '__main__':
    app.run()

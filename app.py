import json
import random
import atexit

from flask import Flask, request

from config import Config
from db.db import DB
from entity.note.bullet_point_note import BulletPointNote
from entity.note.definition_note import DefinitionNote
from entity.note.note import Note
from handler.note_to_question_converter import NoteToQuestionConverter

app = Flask(__name__)
converter = NoteToQuestionConverter()
db = DB()
atexit.register(db.close)


@app.route('/createQuiz')
def createQuiz():
    note = parseNote(str(request.data))
    if type(note.body) == str or random.randint(0, 1) == 0:
        question, answer = converter.convert(note, "short_answer")
    else:
        question, answer = converter.convert(note, "multiple_choice")

    db.connect()
    uuid = db.save_question(question, answer)

    obj = {
        "uuid": uuid,
        "question": question
    }

    return json.dumps(obj.__dict__)


@app.route('/checkAnswer')
def checkAnswer():
    pass


@app.route('/')
def checkConfig():
    print('ENV:      {}'.format(Config.ENV))
    print('COHERE_API_KEY:  {}'.format(Config.COHERE_API_KEY))
    print('HOSTNAME: {}'.format(Config.HOSTNAME))
    print('PORT:     {}'.format(Config.PORT))


def parseNote(text: str) -> Note:
    lines = list(map(lambda x: str(x), text.splitlines()))
    if len(lines) == 1 and lines[0].find(":") != -1:
        parts = lines[0].split(":")
        assert len(parts) == 2
        note = DefinitionNote(parts[0], parts[1])
    elif len(lines) >= 2:
        note = BulletPointNote(lines[0].strip(),
                               list(map(lambda x: x.strip(), lines[1:])))
    else:
        raise AttributeError("Cannot parse request data.")
    return note


if __name__ == '__main__':
    app.run()

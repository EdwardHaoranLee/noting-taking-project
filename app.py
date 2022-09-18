import atexit
import json
import random
import uuid

from flask import Flask, request
from flask_cors import CORS

from db.db import DB
from entity.answer.answer import Answer
from entity.note.bullet_point_note import BulletPointNote
from entity.note.definition_note import DefinitionNote
from entity.note.note import Note
from handler.check_answer_handler import CheckAnswerHandler
from handler.note_to_question_converter import NoteToQuestionConverter

app = Flask(__name__)
CORS(app)
db = DB()

converter = NoteToQuestionConverter()
atexit.register(db.close)


@app.route('/createQuestion', methods=['POST'])
def createQuestion():
    note = parseNote(request.data.decode("utf-8"))
    if type(note.body) == str or random.randint(0, 1) == 0:
        question, answer = converter.convert(note, "short_answer")
    else:
        question, answer = converter.convert(note, "multiple_choice")

    db.connect()
    uuid = db.save_question(question, answer)

    obj = {
        "uuid": str(uuid),
        "question": question.__dict__
    }

    return json.dumps(obj)


@app.route('/checkAnswer')
def checkAnswer():
    text = json.loads(request.data.decode("utf-8"))
    id, user_answer = uuid.UUID(text["uuid"]), Answer(text["answer"])
    db.connect()
    correct_answer = db.get_answer(id)
    return str(CheckAnswerHandler.check_similarity(user_answer, correct_answer)).lower()


@app.route('/')
def test():
    return "hello world"


# def checkConfig():
#     print('ENV:      {}'.format(Config.ENV))
#     print('COHERE_API_KEY:  {}'.format(Config.COHERE_API_KEY))
#     print('HOSTNAME: {}'.format(Config.HOSTNAME))
#     print('PORT:     {}'.format(Config.PORT))


def parseNote(text: str) -> Note:
    text = json.loads(text)["note"]
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

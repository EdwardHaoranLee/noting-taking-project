import os
import uuid
from typing import Tuple

import psycopg2

from entity.answer.answer import Answer
from entity.question.question import Question

SQL_CREATE_TABLE = "CREATE TABLE IF NOT EXISTS questions " \
                   "(id UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(), " \
                   "timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                   "head STRING NOT NULL, " \
                   "body STRING NOT NULL, " \
                   "answer STRING NOT NULL)"
SQL_INSERT = "INSERT INTO questions (head, body, answer) VALUES (%s, %s, %s)"
SQL_SELECT_ID = "SELECT id FROM questions WHERE head = %s AND body = %s AND answer = %s"
SQL_SELECT_ANSWER = "SELECT answer FROM questions WHERE id = %s"
SQL_SELECT_ALL = "SELECT * FROM questions"
SQL_DROP = "DROP TABLE questions"


class DB:
    def __init__(self):
        self.conn = None

    def _exec_statement(self, stmt, values: Tuple[str, ...] = None):
        try:
            if self.conn is None:
                raise ConnectionError("Database is not connected.")
            cur = self.conn.cursor()
            if not values:
                cur.execute(stmt)
            else:
                cur.execute(stmt, values)
            row = cur.fetchall()
            self.conn.commit()
            return row[0] if row else None
        except psycopg2.ProgrammingError:
            return

    def connect(self):
        if self.conn:
            return
        self.conn = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ note_taking")
        self._exec_statement(SQL_DROP)
        self._exec_statement(SQL_CREATE_TABLE)

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def save_question(self, question: Question, correct_answer: Answer) -> uuid.UUID:
        self._exec_statement(SQL_INSERT, (question.head, str(question.body), correct_answer.answer))
        result = self._exec_statement(SQL_SELECT_ID, (question.head, str(question.body), correct_answer.answer))
        return uuid.UUID(result[0])

    def get_answer(self, id: uuid.UUID) -> Answer:
        result = self._exec_statement(SQL_SELECT_ANSWER, tuple([str(id)]))
        return Answer(str(result[0]))

    def _check_table(self):
        print(self._exec_statement(SQL_SELECT_ALL))

    def _clean(self):
        self._exec_statement(SQL_DROP)

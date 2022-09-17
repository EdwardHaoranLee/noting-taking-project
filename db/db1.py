from unittest import result
import uuid
import os
import psycopg2

#from entity.question.question import Question
#from entity.answer.answer import Answer

def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return

# Create a table
def create_tables():
    conn = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ quiz_maker")
    statement = "CREATE TABLE IF NOT EXISTS quiz3 ( \
    id UUID NOT NULL DEFAULT gen_random_uuid(),\
    question STRING NOT NULL,\
    answer STRING NOT NULL \
    )"
    exec_statement(conn, statement)

#def save_question(question: Question, correct_answer: Answer) -> uuid.UUID:

def save_question():
    conn = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ quiz_maker")
    commands = [
        # INSERT a row into the quiz1 table
        "INSERT INTO quiz1 (question, answer) VALUES ('what has 4 legs?', 'a dog')",
    ]

    for command in commands:
        exec_statement(conn, command)
    return id

#def get_answer(self, id: uuid.UUID) -> Answer:
def get_answer(self, Id: uuid.UUID):
    conn = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ quiz_maker")
    conn.cursor().execute("SELECT * FROM quiz1")
    results = conn.cursor().fetchall()
    print(results)
    print('\n')
    return results

# Drop table.
def drop_tables():
    conn = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ quiz_maker")
    conn.cursor().execute("DROP TABLE messages1")
    conn.commit()
    conn.close()

def main():
    # Connect to CockroachDB
    #connection = psycopg2.connect(dsn=os.environ["DATABASE_URL"], application_name="$ db1")
    #connection.cursor().execute("DROP TABLE accounts")
    #connection.commit()

    # Close communication with the database
    #connection.close()


if __name__ == "__main__":
    main()
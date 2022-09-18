from entity.note.note import Note


class DefinitionNote(Note):
    head: str
    body: str

    def __init__(self, head: str, body: str):
        self.head = head
        self.body = body

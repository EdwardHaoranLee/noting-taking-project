from note import Note
from typing import List


class BulletPointNote(Note):
    head: str
    body: List[str]

    def __init__(self, head: str, body: List[str]):
        self.head = head
        self.body = body

    def random_subset(self, n: int) -> List[str]:
        """
        Precondition: n <= len(self.body)

        :param n: the size of subset of body.
        :return: the subset of body
        """


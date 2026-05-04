import random
import string
class NoteFactory:
    @staticmethod
    def create(title=None, content=None):
        return {
            "title": title or NoteFactory._random_string("Note"),
            "content": content or NoteFactory._random_string("Content"),
        }
    @staticmethod
    def create_invalid():
        return {"title": 123, "content": None}
    @staticmethod
    def _random_string(prefix):
        suffix = "".join(random.choices(string.ascii_lowercase, k=6))
        return f"{prefix}_{suffix}"
import requests
class NotesAPI:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    def get_all_notes(self):
        return self.session.get(f"{self.base_url}/notes")
    def create_note(self, data):
        return self.session.post(f"{self.base_url}/notes", json=data)
    def get_note(self, note_id):
        return self.session.get(f"{self.base_url}/notes/{note_id}")
    def update_note(self, note_id, data):
        return self.session.put(f"{self.base_url}/notes/{note_id}", json=data)
    def delete_note(self, note_id):
        return self.session.delete(f"{self.base_url}/notes/{note_id}")
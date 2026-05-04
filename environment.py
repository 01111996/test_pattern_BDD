import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from BDD.pages.notes_api import NotesAPI
def before_all(context):
    context.api = NotesAPI()
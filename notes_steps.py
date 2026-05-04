import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from behave import given, when, then
from BDD.factory.note_factory import NoteFactory
@given("API is running")
def step_api_running(context):
    response = context.api.get_all_notes()
    assert response.status_code == 200, f"API недоступен: {response.status_code}"
@given("there are no notes")
def step_no_notes(context):
    notes = context.api.get_all_notes().json()
    for note in notes:
        context.api.delete_note(note["id"])
@given("there is an existing note")
def step_existing_note(context):
    data = NoteFactory.create()
    response = context.api.create_note(data)
    assert response.status_code == 200
    context.note = response.json()
@when('I create a note with title "{title}" and content "{content}"')
def step_create_note(context, title, content):
    data = NoteFactory.create(title=title, content=content)
    context.response = context.api.create_note(data)
@when("I create a note with invalid data")
def step_create_invalid(context):
    data = NoteFactory.create_invalid()
    context.response = context.api.create_note(data)
@when("I get all notes")
def step_get_all(context):
    context.response = context.api.get_all_notes()
@when("I get note by valid id")
def step_get_valid(context):
    context.response = context.api.get_note(context.note["id"])
@when("I get note by id {note_id:d}")
def step_get_by_id(context, note_id):
    context.response = context.api.get_note(note_id)
@when('I update the note with title "{title}" and content "{content}"')
def step_update(context, title, content):
    data = NoteFactory.create(title=title, content=content)
    context.response = context.api.update_note(context.note["id"], data)
@when('I update note with id {note_id:d} with title "{title}" and content "{content}"')
def step_update_invalid(context, note_id, title, content):
    data = NoteFactory.create(title=title, content=content)
    context.response = context.api.update_note(note_id, data)
@when("I delete the note")
def step_delete(context):
    context.response = context.api.delete_note(context.note["id"])
@when("I delete note with id {note_id:d}")
def step_delete_invalid(context, note_id):
    context.response = context.api.delete_note(note_id)
@then("response status code is {status_code:d}")
def step_status(context, status_code):
    assert context.response.status_code == status_code, (
        f"Ожидался {status_code}, получен {context.response.status_code}: {context.response.text}"
    )
@then('response contains note with title "{title}" and content "{content}"')
def step_note_content(context, title, content):
    note = context.response.json()
    assert note["title"] == title
    assert note["content"] == content
@then("response contains empty list")
def step_empty(context):
    assert context.response.json() == []
@then("response contains at least one note")
def step_not_empty(context):
    assert len(context.response.json()) > 0
@then("response contains the note")
def step_has_note(context):
    assert context.response.json()["id"] == context.note["id"]
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST", "DELETE"])
@login_required
def home():
    if request.method == "POST":
        note_data = request.form.get("note")
        
        if len(note_data) < 1:
            flash("To add a new note it must have some content", category="error")
        else:
            note = Note(data=note_data, user_id=current_user.id)
            
            db.session.add(note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=["DELETE"])
def delete_note():
    if request.method == "DELETE":
        note_id = request.json.get("noteId")
        note = Note.query.get(note_id)
        if note:
            db.session.delete(note)
            db.session.commit()
            flash("Note deleted!", category="success")
        else:
            flash("No note to delete", category="error")

    
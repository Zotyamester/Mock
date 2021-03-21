from app import app, db
from app.models import Answer, City, Question, Registration


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Answer': Answer, 'City': City, 'Question': Question, 'Registration': Registration}

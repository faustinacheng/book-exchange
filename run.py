from BookSwap import app, db
from BookSwap.models import Users, Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Book': Book}

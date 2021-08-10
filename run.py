from BookSwap import app, db
from BookSwap.models import User, Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Book': Book}

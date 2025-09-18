
# we cant import from app bcz we alreaady import from  models,forms.... to app so we create a new file test  to import from  app


from app import app
from database import db


with app.app_context():
    

 # Drop all tables
    db.drop_all()

 # Create all tables (if does not exist)
    db.create_all()





# with app.app_context():
#  books = Book.query.all()
#  for b in books:
#      print(b.id, b.title, b.pages)

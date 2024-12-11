from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import User

# Path to your SQLite database file
db_path = "sqlite:///app.db"

# Create a database engine
engine = create_engine(db_path)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Example: Update `is_admin` to True for a specific user by username
    session.query(User).filter(User.username == 'w1tch').update({User.is_admin: True})
    session.commit()
    print("is_admin updated for specific user!")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()

from app import app, db, Cocktails

# Create the application context
with app.app_context():
    # Create the database tables
    db.create_all()
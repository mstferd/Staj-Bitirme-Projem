from app import app, db
from sqlalchemy import text

def update_image_paths():
    with app.app_context():
        # Update The Witcher
        db.session.execute(
            text("UPDATE content SET image_url = 'static/images/the_witcher.jpg' WHERE title = 'The Witcher'")
        )
        # Update Delibal
        db.session.execute(
            text("UPDATE content SET image_url = 'static/images/Delibal.jpg' WHERE title = 'Delibal'")
        )
        # Update Maleficent
        db.session.execute(
            text("UPDATE content SET image_url = 'static/images/Maleficent.jpg' WHERE title = 'Maleficent'")
        )
        db.session.commit()
        print("Database updated successfully")

if __name__ == "__main__":
    update_image_paths()

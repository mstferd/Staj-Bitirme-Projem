from app import app, db
from sqlalchemy import text

def fix_image_paths():
    with app.app_context():
        # Update paths to match exact filenames
        updates = [
            ("The Witcher", "static/images/The Witcher.jpg"),
            ("Delibal", "static/images/Delibal.webp"),
            ("Maleficent", "static/images/Maleficent.jpg")
        ]
        
        for title, path in updates:
            db.session.execute(
                text("UPDATE content SET image_url = :path WHERE title = :title"),
                {"path": path, "title": title}
            )
        
        db.session.commit()
        print("Image paths updated successfully")

if __name__ == "__main__":
    fix_image_paths()

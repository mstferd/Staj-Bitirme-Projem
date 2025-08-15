from app import app, db, Content

with app.app_context():
    # Find Wednesday in the database (case insensitive search)
    wednesday = db.session.query(Content).filter(
        db.func.lower(Content.title).contains('wednesday')
    ).first()
    
    if wednesday:
        print(f"Found: {wednesday.title}")
        print(f"Current image URL: {wednesday.image_url}")
    else:
        print("No content with 'Wednesday' in title found")

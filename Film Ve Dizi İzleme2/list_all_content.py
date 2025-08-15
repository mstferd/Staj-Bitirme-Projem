from app import app, db, Content

with app.app_context():
    # Get all content
    all_content = Content.query.all()
    
    if all_content:
        print("All content in the database:")
        for content in all_content:
            print(f"ID: {content.id}, Title: {content.title}, Type: {content.type}, Image: {content.image_url}")
    else:
        print("No content found in the database")

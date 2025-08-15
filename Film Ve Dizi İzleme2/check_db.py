from app import app, db, Content

with app.app_context():
    # Find Delibal in the database
    delibal = Content.query.filter(Content.title.like('%Delibal%')).first()
    if delibal:
        print(f"Title: {delibal.title}")
        print(f"Image URL: {delibal.image_url}")
        print(f"Image path: {delibal.image_url.split('static/')[1] if delibal.image_url and 'static/' in delibal.image_url else 'N/A'}")
    else:
        print("Delibal not found in the database")

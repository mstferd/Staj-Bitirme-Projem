from app import app, db, Content

with app.app_context():
    # Find Delibal in the database
    delibal = Content.query.filter(Content.title.like('%Delibal%')).first()
    if delibal:
        print(f"Updating image path for {delibal.title}")
        print(f"Old image URL: {delibal.image_url}")
        delibal.image_url = "static/images/Delibal.jpg"
        db.session.commit()
        print(f"New image URL: {delibal.image_url}")
    else:
        print("Delibal not found in the database")

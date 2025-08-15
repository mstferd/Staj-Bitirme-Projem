from app import app, db, Content

with app.app_context():
    # Check if Wednesday already exists
    if not Content.query.filter(Content.title.ilike('%wednesday%')).first():
        # Add Wednesday to the database
        wednesday = Content(
            title="Wednesday",
            type="series",
            genre="Komedi, Korku, Gizem",
            director="Tim Burton",
            duration=50,
            description="Wednesday Addams, Nevermore Akademisi'ne gider ve orada bir dizi cinayeti çözmeye çalışırken ailesinin karanlık sırlarını da öğrenir.",
            image_url="static/images/Wednesday.jpg"
        )
        db.session.add(wednesday)
        db.session.commit()
        print("Wednesday başarıyla eklendi!")
    else:
        print("Wednesday zaten veritabanında mevcut.")

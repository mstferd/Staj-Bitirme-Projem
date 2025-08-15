from app import app, db, Content

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if we already have content
        if Content.query.first() is None:
            # Add sample movies and series
            movies = [
                Content(
                    title="The Witcher",
                    type="series",
                    genre="Fantastik, Macera",
                    director="Lauren Schmidt Hissrich",
                    duration=60,
                    description="Kıta'da kaderin peşinde bir canavar avcısı olan Geralt, büyücüler ve kralların entrikaları arasında hayatta kalmaya çalışır.",
                    image_url="static/images/the_witcher.jpg"
                ),
                Content(
                    title="Lucifer",
                    type="series",
                    genre="Polisiye, Fantastik",
                    director="Tom Kapinos",
                    duration=45,
                    description="Cehennemin efendisi Lucifer, Los Angeles'ta bir gece kulübü işletmeye ve polisle suç çözmeye başlar.",
                    image_url="static/images/lucifer.jpg"
                ),
                Content(
                    title="Delibal",
                    type="movie",
                    genre="Romantik, Dram",
                    director="Ali Bilgin",
                    duration=117,
                    description="Barış ve Füsun'un tutkulu aşkı, hayatın zorluklarıyla sınanır.",
                    image_url="static/images/Delibal.jpg"
                ),
                Content(
                    title="Avatar",
                    type="movie",
                    genre="Bilim Kurgu, Macera",
                    director="James Cameron",
                    duration=162,
                    description="Pandora gezegeninde geçen destansı bir macera. İnsanlar ve Na'vi'ler arasında bir seçim.",
                    image_url="static/images/Avatar.jpg"
                ),
                Content(
                    title="Inception",
                    type="movie",
                    genre="Bilim Kurgu, Aksiyon",
                    director="Christopher Nolan",
                    duration=148,
                    description="Rüya içinde rüya! Dom Cobb, bilinçaltının derinliklerinde sıradışı bir soygun peşinde.",
                    image_url="static/images/Inception.jpg"
                ),
                Content(
                    title="Ezel",
                    type="series",
                    genre="Dram, Suç",
                    director="Uluç Bayraktar",
                    duration=90,
                    description="İhanete uğrayan Ömer, intikam almak için Ezel kimliğiyle geri döner.",
                    image_url="static/images/Ezel.jpg"
                ),
                Content(
                    title="Maleficent",
                    type="movie",
                    genre="Fantastik, Macera",
                    director="Robert Stromberg",
                    duration=97,
                    description="Uyuyan Güzel masalının karanlık tarafı. Malefiz'in intikam ve affetme hikayesi.",
                    image_url="static/images/Maleficent.jpg"
                ),
                Content(
                    title="Wednesday",
                    type="series",
                    genre="Komedi, Korku, Gizem",
                    director="Alfred Gough, Miles Millar",
                    duration=50,
                    description="Wednesday Addams, Nevermore Akademisi'ne gider ve öğrencileri öldüren bir canavarı durdurmaya çalışırken ailesinin gizemli geçmişini de çözmeye çalışır.",
                    image_url="static/images/Wednesday.jpg"
                )
            ]

            # Add all content to the database
            for movie in movies:
                db.session.add(movie)

            # Commit the changes
            db.session.commit()
            print("Sample content added to the database.")

if __name__ == "__main__":
    init_db()

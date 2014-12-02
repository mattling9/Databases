import sqlite3

def select_all_products():
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from film where FilmID=?",(id,))
        film = cursor.fetchone()
        return film


if __name__ == '__main__':
    films = select_all_products()
    print(films)
    film = select_film(183)
    print(film)
    

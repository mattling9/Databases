import sqlite3

def create_table(db_name,table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to re-create it (y/n):".format(table_name))
            if response == 'y':
                keep_table = False
                print("The {0} table will be recreated - all existing data will be deleted".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

if __name__ == "__main__":
    db_name = "movie.db"
    sql = """create table Product
          (FilmID integer,
          Title text,
          ReleaseYear interger,
          Primary Key(FilmID))"""

    create_table(db_name, "Product", sql)



import sqlite3

def DisplayTable():
        print("Product Table Menu")
        print()
        print("1. (Re)Create Product Table")
        print("2. (Add New Product")
        print("3. Edit existing product")
        print("4. Delete existing Porduct")
        print("5. Search for Products")
        print("0. Quit")
        print()

        
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

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def select_product(productID):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Name,Price from Product where ProductID=?",(productID,))
        product = cursor.fetchone()
        return product

def update_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
                cursor = db.cursor()
                sql = "update Product set Name=?, Price=? where ProductID=?"
                cursor.execute(sql,data)
                db.commit()

def delete_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
                cursor = db.cursor()
                sql = "delete from Product where ProductID = ?"
                cursor.execute(sql,data)
                db.commit()

def select_all_names():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Name from Product")
        productNameList = cursor.fetchall()
        return productNameList
        print()

def select_all_prices():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Price from Product")
        productPriceList = cursor.fetchall()
        return productPriceList
        print()
                
def create_product_table():
        sql = """create table Product
(ProductID interger, Name text, Price real, ProductTypeID interger,
primary key(ProductID), foreign key(ProductTypeID) references ProductType(ProductType))"""
        create_table(db_name, "Product", sql)

def create_product_type_table():
        sql = """create table ProductType 
(ProductTypeID interger, Description text,
primary key(ProductTypeID))"""
        create_table(db_name, "ProductType", sql)


        
if __name__ == "__main__":
    db_name = "Coffee_shop.db"
    sql = """create table Product
          (ProductID integer,
          Name text,
          Price real,
          Primary Key(ProductID))"""
    create_product_table()
    print()
    create_product_type_table()
    print()
    Quit = False
    while not Quit:
        DisplayTable()
        Input = int(input("Enter option here: "))
        print()
        if Input == 1:
                create_table(db_name, "Product", sql)
        elif Input == 2:
                productName = input("Enter Product Name: ")
                productPrice = float(input("Enter Product Price: "))
                print()
                values = (productName, productPrice)
                insert_data(values)
        elif Input == 3:
                productID = int(input("Enter the ID of The Product you Want to edit"))
                select_product(productID)
                productName = input("Enter New Product Name: ")
                productPrice = float(input("Enter New Product Price: "))
                data = (productName, productPrice, productID)
                update_product(data)
        elif Input == 4:
                productID = int(input("Enter ProductID of the Product you Want to delete"))
                data = (productID,)
                delete_product(data)
        elif Input == 5:
                productNameList = select_all_names()
                productPriceList = select_all_prices()
                print("{0}      {1}           {2}".format("ProductID","ProductName","ProductPrice"))
                ProductID = 1
                for item in range(len(productNameList)):
                        print("{0}             {1}           {2}".format(ProductID, productNameList[item], productPriceList[item]))
                        ProductID += 1
        elif Input == 0:
                Quit = True
                        

                
                
                
                
                
                
                
                

        
                
                        
                

                    

              
        

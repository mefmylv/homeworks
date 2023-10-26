import sqlite3

def create_conection(db_file):
    try:
        connenction = sqlite3.connect(db_file)
        return connenction
    except sqlite3.Error as e:
        print(e)

connection = create_conection('hw7.db')


def create_products_table(connection):
    sql_product_table = '''
    CREATE TABLE IF NOT EXISTS products (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Product_Title VARCHAR(200) NOT NULL,
        Price DECIMAL(10,2) NOT NULL DEFAULT 0.0,
        Quantity INTEGER NOT NULL DEFAULT 0
    );
    '''
    cursor = connection.cursor()
    cursor.execute(sql_product_table)
    connection.commit()



def add_products(connection, product_title, price, quantity):
    sql = '''
    INSERT INTO products (Product_Title, Price, Quantity)
    VALUES (?, ?, ?)
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (product_title, price, quantity))
    connection.commit()

def change_quantity(connection, product_ID,new_quantity):
    sql = '''
    UPDATE products SET Quantity = ? WHERE ID = ? '''
    cursor = connection.cursor()
    cursor.execute(sql, (product_ID, new_quantity))
    connection.commit()

def change_price(connection, product_ID,new_price):
    sql = '''Update products Set Price = ? Where ID = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (product_ID, new_price))
    connection.commit()


def del_product(connection, product_ID):
    sql = '''
    DELETE FROM products WHERE ID = ?
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (product_ID,))
    connection.commit()

def print_products(connection):
    sql = '''Select * From products'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print('Продукты:',row)

def choose_product(connection):
    sql = '''
      SELECT * FROM products WHERE Price < 100 AND Quantity > 5;
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("Нет товаров, соответствующих условию.")
        else:
            print("Товары дешевле 100 сомов и с количеством больше 5:")
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print("Ошибка при выборке товаров:", e)

def search_products_by_keyword(connection, keyword):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM products WHERE Product_Title LIKE ?"
        cursor.execute(sql, ('%' + keyword + '%',))
        rows = cursor.fetchall()

        if len(rows) == 0:
            print(f"Нет товаров, содержащих ключевое слово '{keyword}'.")
        else:
            print(f"Товары, содержащие ключевое слово '{keyword}':")
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print("Ошибка при поиске товаров:", e)


create_products_table(connection)

if connection:
    print('connected')

# add_products(connection,'Alpen Gold',100,1)
# add_products(connection,'Coca-Cola',170,2)
# add_products(connection,'Nitro Wildberries',65,1)
# add_products(connection,'Rolton',89,5)
# add_products(connection,'Чипсы Lays со вкусом краба',85,2)
# add_products(connection,'Чипсы Lays со вкусом лука и сметаны',85,1)
# add_products(connection,'Чипсы Lays со вкусом сыра',85,1)
# add_products(connection,'Чипсы Lays со вкусом соли',85,3)
# add_products(connection,'Шампунь Nivea ',245,1)
# add_products(connection,'Кофе', 185,3)
# add_products(connection,'Мыло с запахом мяты',98,6)
# add_products(connection,'Мыло Детское',76,2)
# add_products(connection,'Кетчуп Махеев Лечо',87,1)
# add_products(connection,'Кетчуп 3-делания Чили',56,1)
# add_products(connection,'Молоко 3,2% 1л',85,1)
# add_products(connection,'Сметана 15%',76,2)
change_quantity(connection,5,3)
change_price(connection,5,127.5)
del_product(connection, 10)
choose_product(connection)
search_products_by_keyword(connection, 'Чипсы')
print_products(connection)
connection.close()

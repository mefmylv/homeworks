import sqlite3

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

connection = create_connection('hw8.db')

def country_table(connection):
    sql_country_table = '''
    CREATE TABLE IF NOT EXISTS country (
        ID INTEGER PRIMARY KEY,
        Country_Title TEXT Not NULL
    );
    '''
    cursor = connection.cursor()
    cursor.execute(sql_country_table)
    connection.commit()

def add_countries(connection, country_title):
    sql = '''
    INSERT INTO country (Country_Title)
    VALUES (?)
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (country_title,))
    connection.commit()

def city_table(connection):
    sql_city_table = '''
    CREATE TABLE IF NOT EXISTS City (
        ID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Area FLOAT DEFAULT 0,  
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES country (ID)
    );
    '''
    cursor = connection.cursor()
    cursor.execute(sql_city_table)
    connection.commit()


def add_city(connection, city_title, area, country_id):
    sql = '''
    INSERT INTO City (Title, Area ,country_id)
    VALUES (?, ?, ?)
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (city_title, area, country_id))
    connection.commit()

def employees_table(connection):
    sql_employees_table = '''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES City (ID)
    );
    '''
    cursor = connection.cursor()
    cursor.execute(sql_employees_table)
    connection.commit()

def add_employees(connection, first_name, last_name, city_id):
    sql = '''
    INSERT INTO Employees (First_Name, Last_Name, city_id)
    VALUES (?, ?, ?)
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (first_name, last_name, city_id))
    connection.commit()

def display_cities():
    conn = sqlite3.connect('hw8.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ID, Title FROM City')
    cities = cursor.fetchall()
    conn.close()

    print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"ID: {city[0]} - {city[1]}")


display_cities()

while True:
    chosen_city_id = input("Введите ID города (для выхода введите 0): ")

    if chosen_city_id == '0':
        print("Выход из программы.")
        break

    conn = sqlite3.connect('hw8.db')
    cursor = conn.cursor()
    cursor.execute('SELECT First_Name, Last_Name FROM Employees WHERE city_id = ?', (chosen_city_id,))
    employees = cursor.fetchall()
    conn.close()

    print(f"Сотрудники, проживающие в выбранном городе:")
    for employee in employees:
        print(f"{employee[0]} {employee[1]}")

country_table(connection)
city_table(connection)
employees_table(connection)
if connection:
    print("Connected")
#
# add_countries(connection, 'Japan')
# add_countries(connection, 'South Korea')
# add_countries(connection, 'Italy')
#
# add_city(connection, "Tokyo", 2194.0,1)
# add_city(connection, "Seoul", 605.2,2)
# add_city(connection, "Rome", 1285.0,3)
# add_city(connection, "Bishkek", 187.0,0)
# add_city(connection, "New York", 783.8,0)
# add_city(connection, "Osh", 182.0,0)
# add_city(connection, "Astana", 722.0,0)
#
# add_employees(connection,'Иван','Александров',1)
# add_employees(connection,'Ксения','Иринова', 4)
# add_employees(connection,'Нурсултан','Ильязов',2)
# add_employees(connection,'Тэкэо','Комацу',1)
# add_employees(connection,'Юсо','Чой',2)
# add_employees(connection,'Роджер','Джеймсон',5)
# add_employees(connection,'Бредд','Миллер',4)
# add_employees(connection,'Джон','Смит',5)
# add_employees(connection,'Анастасия','Коноплёва',7)
# add_employees(connection,'Лиза','Алексеева',7)
# add_employees(connection,'Моника','Уолкер',5)
# add_employees(connection,'Минако','Йошимото',1)
# add_employees(connection,'Камеко','Нагадзимо',1)
# add_employees(connection,'Луиджи','Сартин',3)
# add_employees(connection,'Камилла','Боттини',3)

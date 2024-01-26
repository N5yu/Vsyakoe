import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Expenses (
id INTEGER PRIMARY KEY,
name_expenses TEXT NOT NULL,
exp INTEGER
)
''')
connection.commit()
while True:
    h = input("Желаете добавить трату: ")
    if h == "yes":
        name = input("Наименование: ")
        num = int(input("Число: "))
        cursor.execute("INSERT INTO Expenses (name_expenses, exp) VALUES (?, ?)", (name, num))
        connection.commit()
    else:
        print("Операция прерванна")
        break

delete_id = input("Введите ID записи, которую хотите удалить: ")
cursor.execute("DELETE FROM Expenses WHERE id=?", (delete_id,))
connection.commit()

# Выводим обновленные записи в базе данных
cursor.execute('SELECT * FROM Expenses')
exs = cursor.fetchall()
print("Обновленные записи:")
for ex in exs:
    print(ex)

# Выводим общую сумму
cursor.execute('SELECT SUM(exp) FROM Expenses')
total = cursor.fetchall()[0]
print(f"Общая сумма: {total} руб.")

connection.close()
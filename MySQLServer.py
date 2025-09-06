import mysql.connector


try:
    # Connect to MySQL server (adjust host, user, password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS alx_book_store')
            print(f'Database "alx_book_store" created successfully!')
        except Error as e:
            print(f'Error creating database: {e}')
        finally:
            cursor.close()
    else:
        print("Failed to connect to MySQL server.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL server: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

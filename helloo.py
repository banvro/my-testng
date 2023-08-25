import pymysql

# Connection configuration
db_config = {
    "host": "localhost",
    "user": "kristina",
    "password": "!*NG6GRGy@UIU*9r",
    # "database": "abc"
}

# Establish connection
connection = pymysql.connect(**db_config)

# Check if the connection was successful
if connection:
    print("Connected to the MySQL database")

# Close the connection
connection.close()

# GRANT ALL PRIVILEGES ON abc.* TO 'root'@'localhost';

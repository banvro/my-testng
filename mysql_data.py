import mysql.connector

# Replace with your own database information
db_config = {
    "host": "localhost",
    "user": "kristina",
    "password": "!*NG6GRGy@UIU*9r",
    "database": "abc",
    "auth_plugin": "mysql_native_password"
}

# Create a connection
connection = mysql.connector.connect(**db_config)

# Check if the connection was successful
if connection.is_connected():
    print("Connected to the MySQL database")

# Close the connection
connection.close()

# GRANT ALL ON kristina.* TO 'kristina'@'localhost' IDENTIFIED BY 'kristina';
# GRANT ALL ON kristina.* TO 'kristina'@'alm-lt-test.xyz.com' IDENTIFIED BY 'kristina';
# GRANT ALL ON kristina.* TO 'kristina'@'127.0.0.1' IDENTIFIED BY 'kristina';
# GRANT ALL ON kristina.* TO 'kristina'@'172.27.59.54' IDENTIFIED BY 'kristina';
    
# ALTER USER 'kristina'@'localhost' IDENTIFIED BY 'N@rinder123!';

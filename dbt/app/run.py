import mysql.connector
import time

class Database:
    def __init__(self, conInfo) -> None:
        self.conInfo = conInfo

    def connect_with_retry(self, retry_count=5, delay=1):
        for i in range(retry_count):
            try:
                # cnx = mysql.connector.connect(
                #     host="localhost",   # 本地直接执行时，使用localhost
                #     # host="db",         # docker-compose执行时，使用db
                #     user="testuser",
                #     password="123456789",
                #     database="testdb"
                # )
                cnx = mysql.connector.connect(**self.conInfo)
                return cnx
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                print("Retrying in {} seconds...".format(delay))
                time.sleep(delay)
        return None

    def execute(self, command):
        if isinstance(command, list):
            for c in command:
                self.execute(c)
            return
        try:
            print("Executing command ----->>>: {}".format(command))
            cursor.execute(command)
            # cnx.commit()
            records = cursor.fetchall()
            for record in records:
                print(record)
        except mysql.connector.Error as err:
            print("Something went wrong ----->>>: {}".format(err))

    def longterm(self, command):
        if not cursor:
            print("No cursor ERROR")
            return
        if command:
            self.execute(command)
        while True:
            print("-----Enter a command:-----")
            command = input()
            if command == "exit":
                break
            else:
                self.execute(command)



create_commands = [
    """
    CREATE TABLE IF NOT EXISTS employees2 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        age INT,
        email VARCHAR(60)
    )
    """,
    """
    INSERT INTO employees2 (name, age, email) VALUES
    ('John Doe', 30, 'john.doe@example.com'),
    ('Jane Doe', 25, 'jane.doe@example.com'),
    ('Jim Doe', 35, 'jim.doe@example.com')
    """
]


if __name__ == "__main__":

    conInfo = {
        # "host": "localhost",   # 本地直接执行时，使用localhost
        "host":"db",       # docker-compose执行时，使用db
        "user": "testuser",
        "password": "123456789",
        "database": "testdb"
    }

    db = Database(conInfo)

    cnx = db.connect_with_retry()

    if not cnx:
        print("Failed to connect to database")
        exit(1)

    cursor = cnx.cursor()

    # db.execute(create_commands)s
    db.longterm(create_commands)

    cnx.close()


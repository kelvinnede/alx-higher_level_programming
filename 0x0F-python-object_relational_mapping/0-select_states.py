import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
except MySQLdb.Error as e:
    print("Error connecting to MySQL database:", e)
    sys.exit(1)

cursor = db.cursor()

query = "SELECT * FROM states ORDER BY id ASC;"

try:
    cursor.execute(query)
except MySQLdb.Error as e:
    print("Error executing SQL query:", e)
    db.close()
    sys.exit(1)

results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
db.close()

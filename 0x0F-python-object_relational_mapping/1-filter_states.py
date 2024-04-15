#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
        if len(sys.argv) != 4:
                    print("Usage: {} username password database".format(sys.argv[0]))
                            sys.exit(1)

                                username, password, database = sys.argv[1:]

                                    # Connect to MySQL server
                                        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

                                            # Create a cursor object
                                                cursor = db.cursor()

                                                    # Execute SQL query to select states starting with 'N'
                                                        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

                                                            # Fetch all rows
                                                                rows = cursor.fetchall()

                                                                    # Display results
                                                                        for row in rows:
                                                                                    print(row)

                                                                                        # Close cursor and connection
                                                                                            cursor.close()
                                                                                                db.close()


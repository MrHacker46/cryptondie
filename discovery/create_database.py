import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS targets (target_id text PRIMARY_KEY), target_key text \
                target_ip text, target_hostname text, target_city text, target_region text, \
                target_country text, target_location text, target_organization text, target_post text \
                target_timezone"

cursor.execute(create_table)
connection.commit()
connection.close()
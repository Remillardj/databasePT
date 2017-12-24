import sqlite3
from sqlite3 import Error
import time
from datetime import datetime



def start_timer():
	start = time.time()
	return start

def stop_timer(start):
	done = time.time()
	return (done - start)

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print (e)

	return None

def select_all_tasks(conn, table):
	cur = conn.cursor()
	cur.execute("SELECT * FROM table")

	rows = cur.fetchall()
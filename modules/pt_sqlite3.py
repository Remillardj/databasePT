'''
__author__ = "Jaryd Remillard"
__version__ = "1.0.0"
__status__ "InDev"
__date__ "1/6/2018"

'''
# import custom logging configurations
import logging_config as log

try:
	import sqlite3
except:
	log.logger.error("Please install SQLite3")
	exit(1)
import time
from datetime import datetime

def start_timer():
	start = time.time()
	return start

def stop_timer(start):
	done = time.time()
	return (done - start)

def create_connection(db_file):
	start = start_timer()
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		log.logger.error(e)
	log.logger.info("Time to initial connection: " + stop_timer(start))
	return None

def cursor_time():
	start = start_timer()
	cur = conn.cursor()
	log.logger.info("Cursor executed: " + stop_timer(start))

def select_all_tasks(conn, table):
	cur = con.cursor()
	query = "SELECT * FROM " + table
	start = start_timer()
	cur.execute(query)
	log.logger.info("Selecting from all tables query time:" + stop_timer(start_timer))

	start = start_timer()
	rows = cur.fetchall()
	log.logger.info("Fetching all rows: " + stop_timer(start))

def select_table_by_priority(conn, table, tableValue,condition):
	cur = con.cursor()
	start = start_timer()
	query = "SELECT * FROM " + table + " WHERE " + table + "=" + tableValue
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		log.logger.info("Retrieving table by condition: " + stop_timer(start) + " - " + row)

def custom_query(initial, selecting, table, condition=None):
	cur = con.cursor()
	start = start_timer()
	if (condition = None):
		query = initial + " " + selecting + " " + table
	else:
		query = intial + " " + selecting + " " + table + condition
	cur.execute(query)
	rows = cur.fetchall()

# create database connection
def main(sqlite_path=None):
	if (sqlite_path = None):
		database = pass
	else:
		database = sqlite_path

	conn = create_connection(database)
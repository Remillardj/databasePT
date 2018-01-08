'''
__author__ = "Jaryd Remillard"
__version__ = "1.0.0 alpha"
__status__ "InDev"
__date__ "1/7/2018"

'''
# import custom logging configurations
import logging_config as log

try:
	import psycopg2
except:
	log.logger.error("Please install Python module psycopg2")
	exit(1)

try:
	conn = psycopg2.connect("dbname='template' user='dbuser' password='pass")
except:
	log.logger.error("Unable to connect to Postgresql database")

query = "SELECT * FROM table"

cur = conn.cursor()
try:
	cur.execute(query)
except:
	log.logger.erorr("Unable to execute query")
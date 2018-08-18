#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import psycopg2
import random
from sqlite3 import Error
from datetime import datetime

hostname = 'localhost'
username = 'postgres'
password = 'root'
database = 'tact'

def start():
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """    
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    
    rows = None
    try:
        cur = conn.cursor()

        cur.execute( "SELECT * FROM CITY" )
        
        rows = cur.fetchall()
    
    except Error as e:
        print(e)
    
    
    for row in rows :
        print(row)        

        
if __name__ == '__main__':
    start()        
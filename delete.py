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
    
    cur = conn.cursor()
    
    deleted_rows = -1
    try:
        cur.execute("DELETE FROM CITY WHERE ID = %s", ('1'))
        
        # get the number of updated rows
        deleted_rows = cur.rowcount   
             
        print('deleted row : '+str(deleted_rows))
    except psycopg2.IntegrityError as err:
        print("error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('created id : '+str(deleted_rows))

if __name__ == '__main__':
    start()        
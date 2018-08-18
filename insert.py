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
    conn.autocommit = True
    
    city_id = -1
    try:
        cur = conn.cursor()    
        cur.execute("INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES (%s, %s, %s) RETURNING ID", ('Two', 'Two', 'Three'))
        
        city_id = cur.fetchone()[0]       
                
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : {0}".format(error))
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    print('created city id : '+str(city_id))

if __name__ == '__main__':
    start()        
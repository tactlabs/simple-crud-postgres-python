#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import psycopg2

database = "test"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param 
    :return: Connection object or None
    """
    
    hostname = 'localhost'
    username = 'postgres'
    password = 'root'
    database = 'tact'
    
    try:
        conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        conn.autocommit = True
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(e)
 
    return None

def select_all(conn):
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM CITY")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row)         



def add_city(conn, city_obj):
    """
    Create a city
    :param task:
    :return: task id
    """
   
    sql = ''' INSERT INTO CITY (NAME, STATE) 
            VALUES (:name, :state) '''
    cur = conn.cursor()
    
    city_id = -1
    try:
        cur.execute("INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES (%s, %s, %s) RETURNING ID", ('Hello', 'Base', 'Juu'))        
        
        city_id = cur.fetchone()[0]
    except psycopg2.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        if cur is not None:
            cur.close()
    
    return city_id

def update_city(conn, city_obj):
    """
    Create a city
    :param city object:
    :return: None
    """
   
    cur = conn.cursor()
    
    updated_rows = -1
    try:
        cur.execute("UPDATE CITY SET NAME = %s, STATE = %s WHERE ID = %s", (city_obj['name'], city_obj['state'], city_obj['id']))
        
        # get the number of updated rows
        updated_rows = cur.rowcount   
             
        print('updated row : '+str(updated_rows))
        
    except psycopg2.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        if cur is not None:
            cur.close()        
    
    
    
def delete_city(conn, id):
    """
    Delete a city
    :param city object:
    :return: None
    """
   
    cur = conn.cursor()
    
    try:
        cur.execute("DELETE FROM CITY WHERE ID = %s", (id,))
        
        # get the number of updated rows
        deleted_rows = cur.rowcount   
             
        print('deleted row : '+str(deleted_rows))
        
    except psycopg2.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Deleted')
    
def delete_all_cities(conn):
    """
    Delete a city
    :param city object:
    :return: None
    """
   
    sql = ''' DELETE CITY '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql)
        
    except psycopg2.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Delete')        

def main():    
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:        
        
        # CREATE
        print('Create City')
        city_obj = {
            'name' : 'Montreal',
            'state' : 'QC'
        } 
        result = add_city(conn, city_obj)
        print(result)
        print('---------------\n')
        
    
        # READ
        print('Read City')
        select_all(conn)
        print('---------------\n')
        
        
        # UPDATE
        print('Update City')
        city_new_obj = {
            'name' : 'Montreal22',
            'id' : '8',
            'state' : 'ON'
        }
        update_city(conn, city_new_obj)
        print('---------------\n')
        
        
        
        # DELETE    
        print('Delete City')  
        delete_city(conn, 15)
        print('---------------\n')
        
 
 
if __name__ == '__main__':
    main()        
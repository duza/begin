# -*- coding: utf-8 -*-
# using python 2.7.3
''' Program using sql queries forms list kind of (len;num), 
where len - length of segment, rounded to the nearest whole, 
and num - number of segments lenght len. Database "task.db3"
contain table coordinates with fields x1 and x2 - coordinates of
segments on coordinate axis. '''
import sqlite3 as db;

def calclen():
    # retrieving records with the handling, grouping, sorting
    count_len = []
    sql = """ SELECT ROUND(ABS(x1 - x2)+0.5) as len, Count(*) as num 
    FROM coordinates GROUP BY len ORDER BY len; """
    try:
        for tup_len in cu.execute(sql):
            count_len.append(tup_len)
    except Exception as e:
        print "Unexpected error:", e
        co.rollback()
    co.commit()
    return count_len

def clear():
    # delete all records from the table frequencies
    sql = """ DELETE FROM Frequencies; """
    try:
        cu.execute(sql)
    except Exception as e:
        print "Unexpected error:", e
        co.rollback()
    co.commit()

def insert(list_len):
    # adding records to the table frequencies
    try:
        sql = """ INSERT INTO Frequencies (len, num) 
        VALUES(?,?); """
        cu.executemany(sql,list_len)
    except Exception as e:
        print "Unexpected error:", e
        co.rollback()
    co.commit()

def out():
    # select records from the table frequencies
    sql = """ SELECT * FROM Frequencies 
    WHERE len > num; """
    try:
        for el in cu.execute(sql):
            print "{0};{1}".format(*el)
    except Exception as e:
        print "Unexpected error:", e
        co.rollback()
    co.commit()

def main():
    global co
    co= db.connect('task.db3')
    global cu
    cu = co.cursor()
    list_len = calclen()
    clear()
    insert(list_len)
    out()
    co.close()

if __name__ == '__main__':
    main()
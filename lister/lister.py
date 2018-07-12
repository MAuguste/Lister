'''
Created on Jul 11, 2018

@author: MAAUGUSTE
'''

import os
import psycopg2
import psycopg2.extras
#import getpassp
import csv


outputFile = open('missing_files.csv','w', newline='')
outputWrite = csv.writer(outputFile)


try:
    conn = psycopg2.connect(host="localhost", user="postgres", password="Password", dbname="lais")
    #conn = psycopg2.connect(host="lais.goslnet.gov.lc", user="sjnfrancois", passwd="", dbname="lais")
    cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    cur.execute("""SELECT "ID", "Year", "Instrument", "Path", "Status" FROM "Access".poa""")
    rows = cur.fetchall()
    
    for row in rows:      
        if (os.path.exists(row[3])) is False:
        #if (os.path.exists(row.Path)) is False:
            result = [row[0], row[1],row[2], row[3], row[4]]
            desc =(cur.description[3])
            #print (desc)
            outputWrite.writerow(result)
    outputFile.close()   


    cur.close()
    conn.close()           
except Exception as e:
    print(e)

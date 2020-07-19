#!/usr/bin/env python
import os
import snowflake.connector
import sys
import csv
import time

# Gets the version
dirn =  sys.argv[1]
tabn =  sys.argv[2]
ctx = snowflake.connector.connect( user='psvel', password='Un1ver$e', regions='us-east-1', account='MCA49464.us-east-1', warehouse='VEL_WH', database='vel',schema='public' )
cs = ctx.cursor()
for subdir, dirs, files in os.walk(dirn):
    for file in files:
        try:
            cmd="PUT file://"+dirn+"/"+file+" @%"+tabn
            print(cmd)
            cs.execute(cmd)
        except OSError as e:
            if e.errno == 604:
                print("timeout")
                cs.execute("rollback")
            else:
                raise e;
        print("Sleeping for 5 sec...")
        time.sleep( 30 )
ctx.close()

#!/usr/bin/env python
import os
import snowflake.connector
import sys
import csv
import pandas as pd
import numpy as np

# Gets the version
c_size=10000
ctx = snowflake.connector.connect( user='psvel', password='Un1ver$e', regions='us-east-1', account='MCA49464.us-east-1', warehouse='VEL_WH', database='vel' )
cs = ctx.cursor()
#cs.execute("create or replace table testtbl(a int, b string)")
#df = pd.read_csv(sys.argv[1])
for df_chunk in pd.read_csv(sys.argv[1],chunksize=c_size):
    try:
         cs.executemany("insert into emp_usi(empid   , name    , fname   , mname   , lname   , gender  , email   , fatname , motname , motmname, dbo     \
                    , dobt    , age     , weight  , doj     , qoj     , hoj     , yoj     , moj     , mojn    , mojsn   , dojd    , dojw    , dojsd   \
                    , tenure  , sal     , hikeper , ssn     , pno     , place   , ctry    , city    , state   , zip     , region  , uname   , passwd)  \
                    values \
                    (to_number(%s),%s,%s,%s,%s,%s,%s,%s,%s,%s,to_date(%s,'mm/dd/yyyy'),to_time(%s),to_number(%s),to_number(%s),to_date(%s,'mm/dd/yyyy'),\
                    %s,%s,to_number(%s),to_number(%s),%s,%s,to_number(%s),%s,%s,to_number(%s),to_number(%s),\
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",df_chunk.values.tolist()
                    );
    
    except OSError as e:
       if e.errno == 604:
          print("timeout")
          cs.execute("rollback")
       else:
          raise e;
cs.execute("commit")
ctx.close()

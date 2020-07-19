#!/usr/bin/env python
import os
import snowflake.connector
import sys
import csv

# Gets the version
ctx = snowflake.connector.connect( user='psvel', password='Un1ver$e', regions='us-east-1', account='MCA49464.us-east-1', warehouse='VEL_WH', database='vel' )
cs = ctx.cursor()
#cs.execute("create or replace table testtbl(a int, b string)")
with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row:
            try:
#                cs.execute("insert into emp_ins(empid,name) values(%s,%s)",[row[0],row[1]])
                 cs.execute("insert into emp_ins(empid   , name    , fname   , mname   , lname   , gender  , email   , fatname , motname , motmname, dbo     \
                            , dobt    , age     , weight  , doj     , qoj     , hoj     , yoj     , moj     , mojn    , mojsn   , dojd    , dojw    , dojsd   \
                            , tenure  , sal     , hikeper , ssn     , pno     , place   , ctry    , city    , state   , zip     , region  , uname   , passwd)  \
                            values \
                            (to_number(%s),%s,%s,%s,%s,%s,%s,%s,%s,%s,to_date(%s,'mm/dd/yyyy'),to_time(%s),to_number(%s),to_number(%s),to_date(%s,'mm/dd/yyyy'),\
                            %s,%s,to_number(%s),to_number(%s),%s,%s,to_number(%s),%s,%s,to_number(%s),to_number(%s),\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36]]
                            );

            except OSError as e:
               if e.errno == 604:
                  print("timeout")
                  cs.execute("rollback")
               else:
                  raise e;
cs.execute("commit")
ctx.close()

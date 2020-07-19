#!/usr/bin/env python
import os
import snowflake.connector

# Gets the version

ctx = snowflake.connector.connect( user='psvel', password='Un1ver$e', regions='us-east-1', account='MCA49464.us-east-1', warehouse='VEL_WH', database='vel' )
cs = ctx.cursor()
cs.execute("create or replace table testtbl(a int, b string)")
cs.execute("begin")
try:
    cs.execute("insert into testtbl(a,b) values(3, 'test3'), (4,'test4')", timeout=10) 
except ProgrammingError as e:
   if e.errno == 604:
      print("timeout")
      cs.execute("rollback")
   else:
      raise e;
else:
   cs.execute("commit")
   cs.execute("end")
finally:
    cs.close()
ctx.close()

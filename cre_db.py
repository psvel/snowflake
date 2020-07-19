#!/usr/bin/env python
import os
import snowflake.connector

# Gets the version

ctx = snowflake.connector.connect( user='psvel', password='Un1ver$e', regions='us-east-1', account='MCA49464.us-east-1', warehouse='VEL_WH', database='vel' )

cs = ctx.cursor()
try:
#        conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
#        conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
#        conn.cursor().execute("USE DATABASE testdb_mg")
#        conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")
        cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
        cs.execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
        cs.execute("USE DATABASE testdb_mg")
        cs.execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")
        cs.execute("SELECT current_version()")
        cs.execute(
        "CREATE OR REPLACE TABLE "
        "test_table(col1 integer, col2 string)")
        cs.execute(
        "INSERT INTO test_table(col1, col2) VALUES " +
        "    (123, 'test string1'), " +
        "    (456, 'test string2')")
        # Putting Data
        cs.execute("PUT file:///tmp/data/file* @%testtable")
        cs.execute("COPY INTO testtable")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()

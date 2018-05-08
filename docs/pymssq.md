``pymssql`` is one of the most problematic package. It is used extensively as database connection is done via this package. As it uses FreeTDS package, configuration is tricky.
## Installing

### Dependencies
``sudo apt-get install -y unixodbc unixodbc-dev unixodbc-bin libodbc1 odbcinst1debian2 tdsodbc freetds-bin freetds-common freetds-dev libct4 libsybdb5``

### pip
Preferably, python3.6 and newer should be used.

``python3 -m pip uninstall pymssql``

``python3 -m pip install --no-binary pymssql pymssql``

If this doesn't work:

``python3 -m pip install git+https://github.com/pymssql/pymssql``

## Troubleshooting

**For error**: mssql.c:18814:15: error: ‘DBVERSION_80’ undeclared (first use in this function); did you mean ‘DBVERSION_70’? 

In order to solve this issue by using pymssql 2.1.3, I have modified header of ``/usr/include/sybdb.h`` belonging to the libsybdb- devel> package (Cygwin) by adding line below: 

``#define DBVERSION_80 DBVERSION_71``

## Extensive configuration
These steps are very rarely necessary.
### 1
``sudo vim /etc/odbcinst.ini``

```
[ODBC] 
Trace = No 
TraceFile = /tmp/odbc.log  

[FreeTDS] 
Description = FreeTDS 
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so 
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so 
UsageCount = 1
```
### 2
`sudo vim /etc/odbc.ini`
```
[dbserverdsn] 
Driver = FreeTDS 
Server = <server_name>.database.windows.net 
Port = 1433 
Database = <database_name> 
Driver=/usr/local/lib/libtdsodbc.so 
UsageCount = 1 

[Default] 
Driver=/usr/local/lib/libtdsodbc.so 
```
### 3
``sudo vim /etc/freetds/freetds.conf``

```
#   $Id: freetds.conf,v 1.12 2007/12/25 06:02:36 jklowden Exp $ 
# 
# This file is installed by FreeTDS if no file by the same  
# name is found in the installation directory.   
# 
# For information about the layout of this file and its settings,  
# see the freetds.conf manpage "man freetds.conf".   
  
# Global settings are overridden by those in a database 
# server specific section 
[global] 
  # TDS protocol version 
  tds version = 8.0 
  port = 1433 
  
  # Whether to write a TDSDUMP file for diagnostic purposes 
  # (setting this to /tmp is insecure on a multi-user system) 
; dump file = /tmp/freetds.log 
; debug flags = 0xffff 
  
  # Command and connection timeouts 
; timeout = 10 
; connect timeout = 10 
  
  # If you get out-of-memory errors, it may mean that your client 
  # is trying to allocate a huge buffer for a TEXT field.   
  # Try setting 'text size' to a more reasonable limit  
; text size = 64512 
  
# A typical Microsoft server 
[dbserverdsn] 
  database = <database_name> 
  host = <server_name>.database.windows.net 
  port = 1433 
  tds version = 8.0 
  client charset = UTF-8 
```


# Usage
```
# Connection string
# Depending on the freeTDS libraries, tds_version may be changed to 7.0
conn = pymssql.connect(server='',  
    user='',  
    password='',  
    database='',  
    tds_version='8.0',
    port='1433') 

# Get cursor
cursor = conn.cursor() 
# Execute the cursor
cursor.execute("SELECT * FROM TableName") 
# If it is DDL operation conn.commit() will do the trick
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close() 
```

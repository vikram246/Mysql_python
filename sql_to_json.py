import pandas as pd
import pymysql

#parameters for db_connection
db = pymysql.connect(user = 'root',password = '', host = 'localhost', database = 'vikram')

#Query to be execute
sql = "select * from dept"

result = pd.read_sql(sql,con=db)

print ("Required sql data in DF_Format : \n\n" + str(result) + "\n" )

#Converting the result into JSON and SaveAS "result.json"
result.to_json("result.json")

final = result.to_json()

print ("Required JSON format is : \n\n" + str(final) + "\n")




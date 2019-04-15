from  pykafka import KafkaClient
import pandas as pd
import pymysql


client = KafkaClient(hosts="localhost:9092")

db = pymysql.connect(user = 'root',password = '', host = 'localhost', database = 'vikram')
sql = "select * from dept"
result = pd.read_sql(sql,con=db)
final = result.to_json()
client.topics
topics = client.topics['test']


with topics.get_sync_producer() as producer:

    #     for i in range(4):
        producer.produce("Canonical json format :" + str(final))

        print "############## Json produced successfully #############"






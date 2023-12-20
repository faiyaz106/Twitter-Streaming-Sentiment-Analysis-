import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.ml.classification import DecisionTreeClassificationModel

# Available Topics: 'Twitter_Blue_Tick', 'Russia_Ukrain_War', 'Climate Change', 'Elon Musk', 'Football','Cricket'


from twitter import TWITTER_API

tweet=TWITTER_API

querystring = {"list_id":"1591033111726391297","continuation_token":"HBaAgLydmczz0y0AAA==","limit":"100"}
headers = {"X-RapidAPI-Key": "cffedc8ba0m7yftdrsrdfttretrtee4ertfgh1176dp14a29fjsn8f2e2b6580e6",
                   "X-RapidAPI-Host": "twitter154.p.rapidapi.com"}
max_count=5
tweet=TWITTER_API()
tweet.streaming(querystring,headers,max_count)
print('Hello World')



if __name__=="__main__":
    sc=SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc, 60)
    broker_list = 'localhost:9092'
    topic = 'random'
    message= KafkaUtils.createDirectStream(ssc,
                                [topic],
                                {"metadata.broker.list": broker_list})
    words=message.map(lambda x:x[1]).flatMap(lambda x:x.split())
    wordcount=words.map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
    wordcount.ppprint()
    ssc.start()
    ssc.awaitTermination()



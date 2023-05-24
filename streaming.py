import findspark
findspark.init('/etc/spark')
import pyspark
from pyspark import RDD
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.ml.feature import Word2VecModel

# Need to start spark context first
sc=SparkContext(appName="Kafka Spark Streaming")

# Available Topics: 'Twitter_Blue_Tick', 'Russia_Ukrain_War', 'Climate Change', 'Elon Musk', 'Football','Cricket'

# Loading the word2vec model
#wv_path="home/ubuntu/Tstreaming/models/word2vec.model"
#model=Word2VecModel.load(wv_path)

# Loading the decision tree classifier model
#dt_path="home/ubuntu/Tstreaming/models/Decision_Tree.Model"
#dt=DecisionTreeClassificationModel.load(dt_path)

def fun(x):
    print(x)

if __name__=="__main__":
    fun()
    print(fun(x))
    
    
    
    
    
    
    
"""
    ssc = StreamingContext(sc, 60)
    broker_list = 'localhost:9092'
    topic = 'random'
    message= KafkaUtils.createDirectStream(ssc,
                                [topic],
                                {"metadata.broker.list": broker_list})
    
    words=message.map(lambda x:x[1]) #.flatMap(lambda x:x.split())
    #wordcount=words.map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
    words.pprint()
    ssc.start()
    ssc.awaitTermination()





"""






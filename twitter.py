# For running scription: python streaming.py 10    # Here 10 is maximum number to request you want to send
import requests
import datetime
import json
import random
import os
import sys
class TWITTER_API:
    def streaming(self,max_count,**topics):
        os.chdir("../source")
        headers=topics['headers']
        topic_list=[]
        for i in topics:
            if i!='headers':
                topic_list.append(i)        
        count=0
        while (count<max_count):
            topic=random.choice(topic_list)
            querystring=topics[topic]
            url = "https://twitter154.p.rapidapi.com/search/search"
            response = requests.request("GET", url, headers=headers, params=querystring)
            # ct stores current time
            response_dict=response.json()
            response_dict["topic"]=topic
            ct = datetime.datetime.now() 
            x=str(ct).split()
            y=''.join(x[0].split('-'))+''.join((''.join(x[1].split(':'))).split('.'))
            # ts store timestamp of current time
            ts = ct.timestamp()
            file_name='tweet_'+str(y)+'.json'
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(response_dict,f)
                f.close()
            count=count+1
        print('Streaming Stopped')

f=open('topics_query.json','r')
topics=json.load(f)
max_count=int(sys.argv[1])
tweet=TWITTER_API()
tweet.streaming(max_count,**topics)
                    
            
# Twitter-Streaming-Sentiment-Analysis-
1. Building Robust Streaming Data Pipeline
To begin with, we extract Tweets from Twitter via a third-party API from Rapid API. We then integrate the APIs
along Apache NiFi – an open-source tool facilitating easy ingestion and processing of large volumes of streaming
data seamlessly; alongside integrating Kafka (a distributed streaming platform enabling high-speed real-time
processing) followed by Spark Streaming (an efficient tool). Finally, MongoDB comes next since it facilitates
storing & retrieving voluminous amounts of non-relational datasets.
2. Data Preprocessing & Sentiment Prediction Model
Section two processes tweets through feature engineering tasks like stemming or removing stop words while
converting text cases uniformly across all entries in preparation for training ML models capable of performing
sentimental analysis.
We train our model off labeled tweet dataset comprising positive/negative sentiments after running preprocessing
steps above successfully completing them earlier on preprocessed Twitter feeds so when new unseen ones come
later, they're analyzed instantly at runtime.
3. Sentiment Analysis and Visualization
Lastly, section three lets us visualize aggregate sentiment results displayed via a web-based dashboard showing
polarity scores ranging between neutral (-1 scale) up until strongly polarized (+1 range), providing graphical
representations beyond mere pie chart/bar graph displays towards more interactive user experiences suitable
enterprise-level decision making.
Our goal was to build functional pipelines able to handle vast quantities of online content empowering people to
understand attitudes toward different topics. This system can be used for various applications from social media
tracking, and brand reputation management to market research and more – all in real-time.'

Streaming Pipeliene: 
![image](https://github.com/faiyaz106/Twitter-Streaming-Sentiment-Analysis-/assets/25295396/f04c052b-2aeb-484e-911d-69e13b80c388)

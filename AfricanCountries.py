#This code is compiles the Twitter trends in Africa. Below are countries
#That are not utilizing Twitter's API

import twitter
import json

ALGERIA_WOE_ID = 23424740

algeria_trends = twitter_api.trends.place(_id=ALGERIA_WOE_ID)

print(json.dumps(algeria_trends, indent=1)
      
algeria_trends_set = set([trend['name']
                        for trend in algeria_trends[0]['trends']])


GHANA_WOE_ID = 23424824

ghana_trends = twitter_api.trends.place(_id=GHANA_WOE_ID)

print(json.dumps(ghana_trends, indent=1)
      
ghana_trends_set = set([trend['name']
                        for trend in ghana_trends[0]['trends']])


KENYA_WOE_ID = 23424863

kenya_trends = twitter_api.trends.place(_id=KENYA_WOE_ID)

print(json.dumps(kenya_trends, indent=1)
      
kenya_trends_set = set([trend['name']
                        for trend in kenya_trends[0]['trends']])


NIGERIA_WOE_ID = 23424908

nigeria_trends = twitter_api.trends.place(_id=NIGERIA_WOE_ID)

print(json.dumps(nigeria_trends, indent=1)
      
nigeria_trends_set = set([trend['name']
                        for trend in nigeria_trends[0]['trends']])

SOUTH_AFRICA_WOE_ID = 23424942

south_africa_trends = twitter_api.trends.place(_id=SOUTH_AFRICA_WOE_ID)

print(json.dumps(south_africa_trends, indent=1)
      
south_africa_trends_set = set([trend['name']
                        for trend in south_africa_trends[0]['trends']])

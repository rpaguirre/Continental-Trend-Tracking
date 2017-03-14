#This code is compiles the Twitter trends in North America. Ccountries
#That are not utilizing Twitter's API are not listed.

import twitter
import json

CANADA_WOE_ID = 23424775

canada_trends = twitter_api.trends.place(_id=CANADA_WOE_ID)

print(json.dumps(canada_trends, indent=1)
      
canada_trends_set = set([trend['name']
                        for trend in canada_trends[0]['trends']])


DOMINICAN_REPUBLIC_WOE_ID = 23424800
      
dominican_republic_trends = twitter_api.trends.place(_id=DOMINICAN_REPUBLIC_WOE_ID)

print(json.dumps(dominican_republic_trends, indent=1)
      
dominican_republic_trends_set = set([trend['name']
                        for trend in dominican_republic_trends[0]['trends']])


GUATEMALA_WOE_ID = 23424834

guatemala_trends = twitter_api.trends.place(_id=GUATEMALA_WOE_ID)

print(json.dumps(guatemala_trends, indent=1)
      
guatemala_trends_set = set([trend['name']
                        for trend in guatemala_trends[0]['trends']])
      

MEXICO_WOE_ID = 23424900

mexico_trends = twitter_api.trends.place(_id=MEXICO_WOE_ID)

print(json.dumps(mexico_trends, indent=1)
      
mexico_trends_set = set([trend['name']
                        for trend in mexico_trends[0]['trends']])


PANAMA_WOE_ID = 23424924

panama_trends = twitter_api.trends.place(_id=PANAMA_WOE_ID)

print(json.dumps(panama_trends, indent=1)
      
panama_trends_set = set([trend['name']
                        for trend in panama_trends[0]['trends']])


US_WOE_ID = 23424977

us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(json.dumps(us_trends, indent=1)
      
us_trends_set = set([trend['name']
                        for trend in us_trends[0]['trends']])

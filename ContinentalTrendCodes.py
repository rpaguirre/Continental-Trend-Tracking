WORLD_WOE_ID = 1

ASIA_WOE_ID = 24865671
AFRICA_WOE_ID = 24865670
NORTH_AMERICA_WOE_ID = 24865672
SOUTH_AMERICA_WOE_ID = 24865673
ANTARCTICA_WOE_ID = 28289421
EUROPE_WOE_ID = 24865675
PACIFIC_WOE_ID = 24865674

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

asia_trends = twitter_api.trends.place(_id=ASIA_WOE_ID)
africa_trends = twitter_api.trends.place(_id=AFRICA_WOE_ID)
north_america_trends = twitter_api.trends.place(_id=NORTH_AMERICA_WOE_ID)
south_america_trends = twitter_api.trends.place(_id=SOUTH_AMERICA_WOE_ID)
antarctica_trends = twitter_api.trends.place(_id=ANTARCTICA_WOE_ID)
europe_trends = twitter_api.trends.place(_id=EUROPE_WOE_ID)
pacific_trends = twitter_api.trends.place(_id=pacific_trends)

import json

print(json.dumps(world_trends, indent=1)
      
world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

asia_trends_set = set([trend['name']
                       for trend in asia_trends[0]['trends']])

africa_trends_set = set([trend['name']
                         for trend in africa_trends[0]['trends']])

north_america_trends_set = set([trend['name']
                            for trend in north_america_trends[0]['trends']])

south_america_trends_set = set([trend['name']
                            for trend in south_america_trends[0]['trends']])

antarctica_trends_set = set([trend['name']
                             for trend in antarctica_trends[0]['trends']])

europe_trends_set = set([trend['name']
                         for trend in europe_trends[0]['trends']])

pacific_trends_set = set([trend['name']
                          for trend in pacific_trends[0]['trends']])

common_america_trends = north_america_trends_set.intersection(south_america_trends_set)

common_ameriasia_trends = north_america_trends_set.intersection(asia_trends_set)

common_amerieurope_trends = north_america_trends_set.intersection(europe_trends_set)

common_ameriafri_trends = north_america_trends_set.intersection(africa_trends_set)

common_ameriant_trends = north_america_trends_set.intersection(antarctica_trends_set)

common_ameripac_trends = north_america_trends_set.intersection(pacific)trends_set)

print(common_america_trends) #or other intersection trends.

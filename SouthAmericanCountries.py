#This code tracks Twitter's South America's trending topics. Countries not listed are not on Twitter's API


ARGENTINA_WOE_ID = 23424747

argentina_trends = twitter_api.trends.place(_id=ARGENTINA_WOE_ID)

print(json.dumps(argentina_trends, indent=1)
      
argentina_set = set([trend['name']
                        for trend in argentina_trends[0]['trends']])


BRAZIL_WOE_ID = 23424768

brazil_trends = twitter_api.trends.place(_id=BRAZIL_WOE_ID)

print(json.dumps(brazil_trends, indent=1)
      
brazil_set = set([trend['name']
                        for trend in brazil_trends[0]['trends']])


CHILE_WOE_ID = 23424782

chile_trends = twitter_api.trends.place(_id=CHILE_WOE_ID)

print(json.dumps(chile_trends, indent=1)
      
chile_set = set([trend['name']
                        for trend in chile_trends[0]['trends']])


COLOMBIA_WOE_ID = 23424787

colombia_trends = twitter_api.trends.place(_id=COLOMBIA_WOE_ID)

print(json.dumps(colombia_trends, indent=1)
      
colombia_set = set([trend['name']
                        for trend in colombia_trends[0]['trends']])


ECUADOR_WOE_ID = 23424801

ecuador_trends = twitter_api.trends.place(_id=ECUADOR_WOE_ID)

print(json.dumps(ecuador_trends, indent=1)
      
ecuador_set = set([trend['name']
                        for trend in ecuador_trends[0]['trends']])


PERU_WOE_ID = 23424919

peru_trends = twitter_api.trends.place(_id=PERU_WOE_ID)

print(json.dumps(peru_trends, indent=1)
      
peru_set = set([trend['name']
                        for trend in peru_trends[0]['trends']])


VENEZUELA_WOE_ID = 23424982

venezuela_trends = twitter_api.trends.place(_id=VENEZUELA_WOE_ID)

print(json.dumps(venezuela_trends, indent=1)
      
venezuela_set = set([trend['name']
                        for trend in venezuela_trends[0]['trends']])

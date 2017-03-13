#Asia Twitter Trends: Missing countries Afghanistan, Bangladesh, Bhutan, Brunei, Burma (Myanmar),
#Cambodia, China, East Timor, Hong Kong (territory), Iran, Iraq, Kazakhstan, Kyrgyzstan, Laos, Macau (territory),
#Maldives, Mongolia, Nepal, North Korea, Palestinian (territories), Sri Lanka, Syria, Taiwan, Tajikistan,
#Turkmenistan, Uzbekistan, Yemen

import twitter
import json

BAHRAIN_WOE_ID = 23424753

bahrain_trends = twitter_api.trends.place(_id=BAHRAIN_WOE_ID)

print(json.dumps(bahrain_trends, indent=1))

bahrain_trends_set = set([trend['name']
                          for trend in bahrain_trends[0]['trends']])


INDIA_WOE_ID = 23424848

india_trends = twitter_api.trends.place(_id=INDIA_WOE_ID)

print(json.dumps(india_trends, indent=1))

india_trends_set = set([trend['name']
                          for trend in india_trends[0]['trends']])


INDONESIA_WOE_ID = 23424846

indonesia_trends = twitter_api.trends.place(_id=INDONESIA_WOE_ID)

print(json.dumps(indonesia_trends, indent=1))

indonesia_trends_set = set([trend['name']
                          for trend in indonesia_trends[0]['trends']])


ISRAEL_WOE_ID = 23424852

israel_trends = twitter_api.trends.place(_id=ISRAEL_WOE_ID)

print(json.dumps(israel_trends, indent=1))

israel_trends_set = set([trend['name']
                          for trend in israel_trends[0]['trends']])


JAPAN_WOE_ID = 23424856

japan_trends = twitter_api.trends.place(_id=JAPAN_WOE_ID)

print(json.dumps(japan_trends, indent=1))

japan_trends_set = set([trend['name']
                          for trend in japan_trends[0]['trends']])


JORDAN_WOE_ID = 23424860

jordan_trends = twitter_api.trends.place(_id=JORDAN_WOE_ID)

print(json.dumps(jordan_trends, indent=1))

jordan_trends_set = set([trend['name']
                          for trend in jordan_trends[0]['trends']])


KUWAIT_WOE_ID = 23424870

kuwait_trends = twitter_api.trends.place(_id=KUWAIT_WOE_ID)

print(json.dumps(kuwait_trends, indent=1))

kuwait_trends_set = set([trend['name']
                          for trend in kuwait_trends[0]['trends']])



LEBANON_WOE_ID = 23424873

lebanon_trends = twitter_api.trends.place(_id=LEBANON_WOE_ID)

print(json.dumps(lebanon_trends, indent=1))

lebanon_trends_set = set([trend['name']
                          for trend in lebanon_trends[0]['trends']])


MALAYSIA_WOE_ID = 23424901

malaysia_trends = twitter_api.trends.place(_id=MALAYSIA_WOE_ID)

print(json.dumps(malaysia_trends, indent=1))

malaysia_trends_set = set([trend['name']
                          for trend in malaysia_trends[0]['trends']])


OMAN_WOE_ID = 23424898

oman_trends = twitter_api.trends.place(_id=OMAN_WOE_ID)

print(json.dumps(oman_trends, indent=1))

oman_trends_set = set([trend['name']
                          for trend in oman_trends[0]['trends']])


PAKISTAN_WOE_ID = 23424922

pakistan_trends = twitter_api.trends.place(_id=PAKISTAN_WOE_ID)

print(json.dumps(pakistan_trends, indent=1))

pakistan_trends_set = set([trend['name']
                          for trend in pakistan_trends[0]['trends']])


PHILLIPINES_WOE_ID = 23424934

phillipines_trends = twitter_api.trends.place(_id=PHILLIPINES_WOE_ID)

print(json.dumps(phillipines_trends, indent=1))

phillipines_trends_set = set([trend['name']
                          for trend in phillipines_trends[0]['trends']])


QATAR_WOE_ID = 23424930

qatar_trends = twitter_api.trends.place(_id=QATAR_WOE_ID)

print(json.dumps(qatar_trends, indent=1))

qatar_trends_set = set([trend['name']
                          for trend in qatar_trends[0]['trends']])


RUSSIA_WOE_ID = 23424936

russia_trends = twitter_api.trends.place(_id=RUSSIA_WOE_ID)

print(json.dumps(russia_trends, indent=1))

russia_trends_set = set([trend['name']
                          for trend in russia_trends[0]['trends']])


SAUDI_ARABIA_WOE_ID = 23424938

saudi_arabia_trends = twitter_api.trends.place(_id=SAUDI_ARABIA_WOE_ID)

print(json.dumps(saudi_arabia_trends, indent=1))

saudi_arabia_trends_set = set([trend['name']
                          for trend in saudi_arabia_trends[0]['trends']])


SINGAPORE_WOE_ID = 23424948

singapore_trends = twitter_api.trends.place(_id=SINGAPORE_WOE_ID)

print(json.dumps(singapore_trends, indent=1))

singapore_trends_set = set([trend['name']
                          for trend in singapore_trends[0]['trends']])


SOUTH_KOREA_WOE_ID = 23424868

south_korea_trends = twitter_api.trends.place(_id=SOUTH_KOREA_WOE_ID)

print(json.dumps(south_korea_trends, indent=1))

south_korea_trends_set = set([trend['name']
                          for trend in south_korea_trends[0]['trends']])


THAILAND_WOE_ID = 23424960

thailand_trends = twitter_api.trends.place(_id=THAILAND_WOE_ID)

print(json.dumps(thailand_trends, indent=1))

thailand_trends_set = set([trend['name']
                          for trend in thailand_trends[0]['trends']])


TURKEY_WOE_ID = 23424969

turkey_trends = twitter_api.trends.place(_id=TURKEY_WOE_ID)

print(json.dumps(turkey_trends, indent=1))

turkey_trends_set = set([trend['name']
                          for trend in turkey_trends[0]['trends']])


UNITED_ARAB_EMIRATES_WOE_ID = 23424738

united_arab_emirates_trends = twitter_api.trends.place(_id=UNITED_ARAB_EMIRATES_WOE_ID)

print(json.dumps(united_arab_emirates_trends, indent=1))

united_arab_emirates_trends_set = set([trend['name']
                          for trend in united_arab_emirates_trends[0]['trends']])


VIETNAM_WOE_ID = 23424984

vietnam_trends = twitter_api.trends.place(_id=VIETNAM_WOE_ID)

print(json.dumps(vietnam_trends, indent=1))

vietnam_trends_set = set([trend['name']
                          for trend in vietnam_trends[0]['trends']])


#Figures out the commonalities throughout Asia
common_asian_trends = bahrain_trends_set.intersection(india_trends_set, indonesia_trends_set, israel_trends_set,
                                                      japan_trends_set, jordan_trends_set, kuwait_trends_set,
                                                      lebanon_trends_set, malaysia_trends_set, oman_trends_set,
                                                      pakistan_trends_set, phillipines_trends_set, qatar_trends_set,
                                                      russia_trends_set, saudi_arabia_trends_set, singapore_trends_set,
                                                      south_korea_trends_set, thailand_trends_set, turkey_trends_set,
                                                      united_arab_trends_set, vietnam_trends_set)

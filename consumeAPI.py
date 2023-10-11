import requests

response = requests.get(
    'http://api.stackexchange.com/2.2/questions?order=desc&\
    sort=activity&site=stackoverflow')

for q in response.json()['items']:
    if q['answer_count'] == 0:
        print(q['title'])
        print(q['link'])
    else:
        print('skipped')
    print()

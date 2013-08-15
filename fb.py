/*
Author: Khushal Singh Rajawat
*/



import requests
import json


AFTER = 1353233754
//This is the access token which can be generated using the graph api after you are logged into facebook
TOKEN = 'CAACEdEose0cBAGtWmrWrjOXGMDNAnHZCwbdWs7Rc7Ua5KT5QDlkYNCnzYwZBwQmSzpMNfS4LTAX5otFeULZA78sAQOyWLiAKgRNZCCAIkBZA5ElWUcwyLjnUsevpkmsgcZCTBL1fRZBZA11se6tZBJLniSDQTrfotYzwZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time > 1353233754 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
   
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
        message = 'Thanks %s :)' % user['first_name']
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)

        print ("Wall post %s done" % wallpost['post_id'])

if __name__ == '__main__':
    commentall(get_posts());

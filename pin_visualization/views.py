from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
import json
import itertools
import urllib
from urllib.request import urlopen
import requests
from collections import Counter
import re

#wACCESS_TOKEN = "6538dd91635442d38d77cecb53cf5e87"
ACCESS_TOKEN = "254844933.1afb706.9fb7166d26ce4345ad9ea270ae865a06"
CLIENT_ID = "1afb706cfcc847dcb8b5a6bbe5babd0c"
BASE_API = "https://api.instagram.com"
URL = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=%s' % ACCESS_TOKEN

# def get_request(path, params=None):
#     if params:
#         params.update({'access_token': ACCESS_TOKEN})
#     else:
#         params = {'access_token': ACCESS_TOKEN}
#     url = "%s%s?%s" % (BASE_API, path, urllib.parse.urlencode(params))
#     result = urlopen(url)
#     response_data = result.read().decode('utf-8')
#     obj = json.loads(response_data)
#     return obj


# def get_insta_media():
    # data = get_request('/v1/users/self/?access_token={}'.format(ACCESS_TOKEN))
    # returns list of pins, each pin is object with 'note' field
    # pins = data['data']
    # # i want to iterate through each pin and capture text of 'note' attribute
    # for pin in pins:
    #     text = pin['note'].split(' ')
    #     notes.append(text)
    # merged_notes = list(itertools.chain(*notes))
    # # uniques = [word for word in merged_notes if word not in stopwords.words('english')]
    # for word in merged_notes:
    #     if word.lower() not in OPERATORS and word.isalpha():
    #         uniques.append(word)
    # uniq_words = sorted(set(uniques))
    # counts = Counter(uniques)
    # # return the the top_n results (using print for demonstration)
    # print(counts.most_common(top_n))
    # data = 'https://api.instagram.com/v1/users/self/?access_token={}'.format(ACCESS_TOKEN)
    # obj = json.loads(data)
    # print(obj)

def home(request):
    # image_orig = []
    # img_src = []
    img_links = []
    # img_links2 = []
    # data = open('pins/fixtures/pins_formatted.json').read()
    # obj = json.loads(data)

    # for pin in obj:
    #     image_orig.append(pin)

    # for ele in image_orig:
    #     img_src.append(ele['images']['orig']['url'])
    #     img_links.append(ele['link'])

    # img_combined = zip(img_src, img_links)

    response = requests.get(URL).json()
    response_data = response["data"]
    for response_data in response["data"]:
        for image in response_data['images']['standard_resolution']['url']:
            # join = ''.join(image)
            # join.split('http')
            img_links.append(image)
    # image_dict = dict(i, img_links.count(i) for i in img_links)
    combo=''.join(img_links)
    # combo2= list(filter(None, re.split("https")))
    combo2=combo.split('https')
    combo3=[]
    for item in combo2:
        combo3.append("https"+item)
    del(combo3[0])

    # img_combined = zip(combo3, combo3)
    # print(img_combined[0])
    #         # img_links2.append(image)
    # img_combined = zip(img_links, img_links2)
    # return HttpResponse(img_links, "text/html")
    # obj = json.loads(data)
    # print(img_combined)

    # print(img_links)
    # print(len(img_links))
    
    # return render(request, 'pins/pin_view.html', {"urls": img_combined})
    return render(request, 'pins/pin_view.html', {"combo3": combo3 })

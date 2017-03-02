from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
import json
import itertools


def home(request):
    image_orig = []
    img_src = []
    img_links = []
    data = open('pins/fixtures/pins_formatted.json').read()
    obj = json.loads(data)

    for pin in obj:
        image_orig.append(pin)

    for ele in image_orig:
        img_src.append(ele['images']['orig']['url'])
        img_links.append(ele['link'])

    img_combined = zip(img_src, img_links)

    # print(img_links)
    # print(len(img_links))
    
    return render(request, 'pins/pin_view.html', {"urls": img_combined})

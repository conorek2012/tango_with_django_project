import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
        'views':10,
        "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
        'views':100,
        "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
        'views':16,
        "url":"http://www.korokithakis.net/tutorials/python/"} ]


    django_pages = [
        {"title":"Official Django Tutorial",
        'views':87,
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
        'views':37,
        "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
        'views':56,
        "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle",
        'views':50,
        "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
        'views':6,
        "url":"http://flask.pocoo.org"} ]

    cats = {'Python': {"pages": python_pages, 'fields': {"name":"Python","views":128, "likes":64}},
            'Django': {"pages": django_pages,'fields': {"name":"Django","views":64, "likes":32}},
            'Other Frameworks': {"pages": other_pages, 'fields': {"name":"Other Frameworks","views":32, "likes":16}}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['fields'])
        for p in cat_data["pages"]:
            print (p)
            add_page(c, p["title"], p["url"], p["views"])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, fields):
     c = Category.objects.get_or_create(name=name)[0]
     c.views = fields['views']
     c.likes = fields['likes']
     c.save()
     return c


if __name__ == '__main__':
     print("Starting Rango population script...")
     populate()

from app_curd import models
from django.db.models import Q
import re

def search(query):
    if query == None:
        objs=[]
    else:
        if re.search(r'[1-9]\d{3}-\d{2}-\d[1-9]',query,re.S) != None:
            objs = models.obj.objects.all().filter(
                Q(name__contains=query)|Q(gender__contains=query)|
                Q(id_number=query)|Q(brithday__contains=query)
            )
        else:
            objs = models.obj.objects.all().filter(
                Q(name__contains=query)|Q(gender__contains=query)|
                Q(id_number=query)
            )
        print(type(objs))
    return objs
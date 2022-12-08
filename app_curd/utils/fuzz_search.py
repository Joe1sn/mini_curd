from app_curd import models
from django.db.models import Q
import re

def search(query):
    if query == None:
        objs=[]
    else:
        if query in ["Male","male","Femal","female"]:
            if query=="Male" or "male": 
                query = 1
            elif query == "Female" or "female": 
                query = 0
            objs = models.obj.objects.all().filter(
                Q(gender=query)
            )

        elif re.findall(r'[1-9]\d{3}-\d{2}-\d[1-9]',query) != []:
            from datetime import date
            brithday = re.findall(r'[1-9]\d{3}-\d{2}-\d[1-9]',query)[0].split("-")
            brithday = date(int(brithday[0]),int(brithday[1]),int(brithday[2]))            
            objs = models.obj.objects.all().filter(
                Q(name__contains=query)|Q(id_number=query)|Q(brithday=brithday)
            )
        else:
            objs = models.obj.objects.all().filter(
                Q(name__contains=query)|Q(gender__contains=query)|Q(id_number=query)
            )
            
    return objs
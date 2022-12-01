from app_curd import models
import time

def search(query):
    # seconds = time.perf_counter()
    if query == "1":
        objs = models.obj.objects.all().order_by("name")
    elif query == None:
        objs=[]
    else:
        objs = models.obj.objects.all().order_by("id")
    # seconds = format((time.perf_counter() - seconds)*1000,".3f")    #--- end time ---
    # count = objs.count()
    return objs#,seconds,count
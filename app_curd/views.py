from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from app_curd import models
import time

objs = []
page_obj = []
seconds = "NaN"
counts = "NaN"
page = 1

@login_required(login_url='/login/')
def index(request):
    global page_obj
    global objs
    global seconds
    global counts

    if request.method == 'POST':
        query = request.POST.get("query")
        seconds = time.perf_counter()   #--- start time ---

        query = query.split(" ")
        objs = models.obj.objects.all().order_by("id")

        seconds = format((time.perf_counter() - seconds)*1000,".3f")    #--- end time ---
        counts = models.obj.objects.count()

    result_table = str(get_page(request=request).content,encoding="utf-8")
    return render(request,"index.html",{"result_table":result_table, "seconds":seconds, "counts":counts})

@login_required(login_url='/login/')
def get_page(request):
    global page_obj
    #根据 `objs` 生成多页
    # 使用request.GET.get()函数获取url中的page参数的数值。默认第1页
    try:
        page = request.GET.get('page')
    except:
        page = 1
    # 生成Paginator对象对数据分页，每页显示x条数据
    paginator = Paginator(objs,2)

    # 获取查询页数的接口数据列表，page()函数会判断page实参是否是有效数字
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except (EmptyPage, InvalidPage):
        # 创建最终的page对象
        page_obj = paginator.page(paginator.num_pages)
    return render(request,"get_page.html",{"objs":page_obj,})
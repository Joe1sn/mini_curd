from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from app_curd.utils.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from app_curd import models
from app_curd.utils.fuzz_search import search
from math import *


#查询页面
@login_required(login_url='/login/')
def index(request):
    page = get_page(request=request)
    result_table = str(page.content,encoding="utf-8")
    return render(request,"index.html",{"result_table":result_table,})

# ToDo:
#  - 输入页面翻页
@login_required(login_url='/login/')
def get_page(request):

    try:
        query = request.GET.get('query')
    except:
        query = ""
    
    #根据 `objs` 生成多页
    # 使用request.GET.get()函数获取url中的page参数的数值。默认第1页 ceil(objs.count()/pre_page)
    try:
        page = request.GET.get('page')
    except:
        page = "1"
    if page == None:
        page = "1"
    page_num = int(page)    #当前页数
    pre_page = 5            #每页元素数目
    slice_max = 3           #最大同时页数
    max_page = 1            #最大页数
    min_page = 1            #最小页数
    not_reach_max_flag = True  #同时页数是否超过最大页
    # 查询结果并分页 
    # 生成Paginator对象对数据分页，每页显示x条数据
    if query != None:
        objs = search(query)    #查询
        max_page = ceil(objs.count()/pre_page)
        # max_page = ceil(len(objs)/pre_page)
        if slice_max >= max_page:
            slice_max = max_page
            not_reach_max_flag = False
            paginator = Paginator(objs,pre_page)

        elif page_num < ceil(slice_max/2):
            paginator = Paginator(objs,pre_page,start=1,end=slice_max)
        elif page_num <= max_page - ceil(slice_max/2):
            paginator = Paginator(objs,pre_page,start=page_num-int(slice_max/2),end=page_num+int(slice_max/2))
        else:
            paginator = Paginator(objs,pre_page,start=max_page-slice_max+1,end=max_page)

    else:
        objs = []#paginator.num_pages
        paginator = Paginator(objs,1)
        
    # paginator = Paginator(objs,1)
    # 获取查询页数的接口数据列表，page()函数会判断page实参是否是有效数字
    try:
        page_obj = paginator.page(page)
        
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except (EmptyPage, InvalidPage):
        # 创建最终的page对象
        page_obj = paginator.page(paginator.num_pages)

    return render(request,"get_page.html",{
        "objs":page_obj,
        "max_page":max_page-int(slice_max/2),
        "min_page":min_page+int(slice_max/2),
        "not_reach_max":not_reach_max_flag
    })

#添加页面
# Todo:
#  - 添加照片上传
#  - 添加excel表格批量导入

@login_required(login_url='/login/')
def add(request):
    msg = ""
    error_msg = '<div class="alert alert-danger" role="alert"><strong>Error!</strong> your input data is not legal</div>'
    warning_msg = '<div class="alert alert-warning" role="alert"><strong>Warning!</strong> data is duplicated</div>'
    ok_msg = '<div class="alert alert-success" role="alert"><strong>OK!</strong> add success</div>'

    if request.method == "POST":
        name = request.POST.get("name")
        id_number = request.POST.get("id_number")
        brithday = request.POST.get("brithday")
        gender = request.POST.get("gender")
        print(name,id_number,brithday,gender)
        print(type(name),type(id_number),type(brithday),type(gender))
        if name == "" or id_number == "" or len(id_number)!=13:
                msg = error_msg
        else:
            if models.obj.objects.filter(id_number=id_number):
                msg = warning_msg
            else:
                from datetime import datetime,date,timedelta
                if brithday != None:
                    brithday = brithday.split("-")
                    brithday = date(int(brithday[0]),int(brithday[1]),int(brithday[2]))
                    today = date.today()
                    if brithday > today or today - brithday > timedelta(days=365*150):
                        msg = error_msg
                    else:
                        models.obj.objects.create(
                            id_number = id_number,name = name,
                            brithday = brithday, gender = gender
                        )
                        msg = ok_msg
    return render(request,"add.html",{"msg":msg})





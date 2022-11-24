# MINI_CURD

一个基础的 Django 自用小型框架，主要实现的功能就是对数据的 **增删查改** + **登录框**

不采用前后端分离设计，数据库使用mysql

## TODO

- 前端
    - [x] `login.html`
    - [x] `index.html`
    - [x] `bootstrap/CSS/JS/JQuery`
        - [x] bootstrap 资源导入
        - [x] CSS 导入与添加
        - [x] JS 导入与添加
- 后端
    - [x] ORM Model
    - [x] login form
    - **CURD**
        - [ ] Create
        - [ ] Update
        - [ ] Read
        - [ ] Delete
- 文档
    - `login`

        使用django自带的auth进行验证

        如果已经登陆则重定向到 `index`

        - DTL相关
            - 网页表头 `name`
        - 提交的参数 
            使用django form组件，位于 `app_curd\forms.py`中


    - `index` 
        - DTL相关
            - 查询使用秒数 `seconds`
            - 返回的结果总数 `counts`
            - 返回地对象 `objs`
        - 提交的参数
            - 模糊查询语句 `query`


- 数据库
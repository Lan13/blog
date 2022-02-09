# Django编写的简易个人博客 

## 环境要求

- python 3.9.0
- Pycharm Community 2021.1.3
- mysql 8.0.26
- Django 4.0.1
- Markdown 3.3.6
- Pillow 9.0.1
- Pygments 2.11.2
- django-bootstrap4 21.2
- django-imagekit 4.1.0
- mysqlclient 2.1.0
- django-simple-captcha 0.5.14

## 程序结构

- Blog

  Blog为程序项目

- blogs

  blogs为应用程序，包含文章等信息

- comments

  comments为应用程序，包含评论等信息

- users

  users为应用程序，包含用户等信息

## 目前已实现的功能

1. 文章发表、文章修改、文章查看
2. 发表评论、修改评论
3. 用户注册、用户登录、用户退出、修改密码
4. 用户个人主页、编辑个人介绍、上传个人头像
5. markdown渲染博客（代码高亮貌似有点问题- - 看html没什么问题，但是我的浏览器没办法显示高亮）
6. 分页展示

-------

7. 验证码、刷新验证码

## 功能展示

NOTICE：建议克隆到本地查看效果

首页为：<img src="images\welcome.png"/>

用户注册界面：<img src="images\register.png"/>

用户登录界面：<img src="images\login.png"/>

用户登录之后：右上角会显示用户名<img src="images\index.png"/>

全部博客：这里可以查看所有用户的所有博客<img src="images\blogs.png"/>

查看博客：当用户已经登录时，可以在博客的下方评论<img src="images\blog.png"/>

如果没有登录的话，会显示一个需要登录才能评论的信息：<img src="images\comment.png"/>

个人主页：（实在不会布局QwQ）<img src="images\homepage.png"/>

导航栏的下拉框：<img src="images\dropdown.png"/>

（只有为超级用户时才有到django后台的链接）

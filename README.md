```
python操作
pip freeze > requirements.txt
pip install -r requirements.txt
# 环境
mkvirtualenv -p python3 XXX
workon XXX # 进入虚拟环境
deactivate # 退出虚拟环境
rm virtualenv XXX # 删除该虚拟环境
# 开始django项目
django-admin startproject xxx
# 创建目录
mkdir apps media static templates extra_apps
# 使用稳定的XADMIN和DjangoUeditor
# 创建APP
python manage.py startapp xxx
```



```
# 同步数据库
python manage.py makemigrations
# 生成表
python manage.py migrate
# 创建超级管理员和密码
python manage.py createsuperuser
# 部署静态文件
python manage.py collectstatic
```

```
git add 
git commit -m "xx"
git push origin master
git reset --hard
git pull
```

```
uwsgi -i uwsgi.ini &

pkill -9 uwsgi

uwsgi --ini uwsgi.ini

```

## 

一个mysql容器编排，用于测试简单的SQL语句。

### 1. 启动服务

首先，去run.py中把连接的host改为db

然后运行如下命令启动

```bash
# 启动容器编排
docker-compose up --build -d
# 连接日志
docker-compose logs db > db.txt
docker-compose logs app > app.txt
```

### 2. 连接数据库

新建一个终端，使用如下命令查看容器id，并连接stdin

```bash
# 查看容器id
docker ps -a
# 连接stdin
docker attach <container_id>
```
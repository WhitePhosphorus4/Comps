## 

本机docker、docker-compose和redis测试脚本


### 1. 启动服务

```bash
# 启动容器编排
docker-compose up --build -d
# 连接日志
docker-compose logs redis > redis_logs.txt
docker-compose logs webapp > webapp_logs.txt
```

### 2. 连接并进行测试

因为是用flask写了个简易网站，因此直接访问`http://localhost:8000`即可进行测试。

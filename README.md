### jenkins workspace clean:

- 遍历jenkins节点的workspace，获取jenkins job name
- 如果该job不存在（调用jenkinsapi实现），则删除相应的workspace
- 需要对jenkins每个节点进行处理
- 需要python2.7

### 其他
- python2.6升级到2.7：http://blog.csdn.net/jcjc918/article/details/11022345
- setuptools安装：http://blog.csdn.net/turkeyzhou/article/details/8880887

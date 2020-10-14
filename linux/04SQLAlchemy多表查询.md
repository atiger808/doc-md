# SQLAlchemy多表查询

`20:30上课！！！`

#####1.多表查询

##### 2.原生SQL的查询

##### 3.序列化



### 1.多表查询

在MySQL中我们讲了多表查询，在`SQLAlchemy`中也有多表查询的概念

```python
#不一定两张表有外键关系才可以一起关联查询，只要给出关联条件就可以
rows = session.query(User.id,User.name,Column_test.id,Column_test.name).filter(User.id==Column_test.id).all()

#也可以使用join
rows = session.query(Student.name,User.number).join(User,Student.name==User.name).all()
print(rows)

#outerjoin代表left join ，在SQLAlchemy中没有右连接
rows = session.query(Student.name,User.number).outerjoin(User,Student.name==User.name).all()

#对于union也是可以使用的
q1 = session.query(Student.name)
q2 = session.query(User.name)
rows = q1.union(q2).all()

#子表查询
from sqlalchemy import func
q3 = session.query(Student.dep_id,func.count('*').label('dep_count')).group_by(Student.dep_id).subquery()
print(q3)
rows = session.query(Department,q3.c.dep_count).outerjoin(q3,q3.c.dep_id==Department.id).all()
print(rows)
#这里注意，使用查询子表查询的时候使用  q3.c.dep_count  这种方式去取得对应的属性
#subquery 就是子查询的意思
#group_by  having  order_by 等这些都是可用的
#label 是标签的意思，这里的作用类似与MySQL中的as
#如果要使用聚合函数，需要导入func模块，导入之后就可以是使用各种函数，只要连接的数据库支持
#这个查询，几乎把我们常会用到的各种情况给演示出来，加上之前我们讲过的一些查询，我们在工作中可能会遇到的查询，基本上都已经讲解
```

多表查询使用`SQL Alchemy`同样也可以达到我们写`SQL`才能做到的事情，要是要想熟练掌握，需要自己多练习，多尝试。



### 2.原生SQL的查询

在实际的使用过程中，有些时候可能会遇到用SQLAlchemy不能够很好利用数据库的特性，或者需要写很多关联的时候，我们也可以写原生的SQL，然后使用SQLAlchemy去执行。

```python
sql_0 = """ 
SELECT
    * 
FROM
    `user`
"""
#print(dir(session))
rows = session.execute(sql_0)
#print(rows,type(rows),dir(rows))
r = rows.fetchone()
print('***',r)
for i in rows:
	print('===',i)
#这里的 execute 便是执行原生SQL的方法
#fetchone 是每次取一条数据的意思
#可以通过循环把这张表的数据依次全部取完
```

在同样可以传递参数

```python
sql_1 = """ 
SELECT
    *
FROM
    student
WHERE
    dep_id = :id 
"""
rows = session.execute(sql_1,{'id':1})
r = rows.fetchall()
print(r)
for i in r:
    print(i)

#这里的 fetchall 是全部取出的意思，也可以通过for循环给依次打印出来   
#这里的 :id  是其语法规则，但是这里的 sql_1 是个字符串，我们可以使用字符串拼接或者格式化输出的方式来传递变量
sql_1 = """ 
SELECT
    *
FROM
    student
WHERE
    dep_id = %s
"""%(1)
#或者
sql_1 = """ 
SELECT
    *
FROM
    student
WHERE
    dep_id = {}
""".format(1)
#如果使用字符串的方法，那么 execute 需要改成如下的形式
rows = session.execute(sql_1)
```

使用`execute`也可以执行更新，删除和插入操作

```python
sql_2 = """ 
UPDATE `user`
SET age = %s 
WHERE
    id = %s ;
"""%(18,1)
rows = session.execute(sql_2)
print(rows)
```



### 3.序列化

如果希望透明地存储 Python 对象，而不丢失其身份和类型等信息，则需要某种形式的对象序列化：它是一个将任意复杂的对象转成对象的文本或二进制表示的过程。同样，必须能够将对象经过序列化后的形式恢复到原有的对象。

####`Json`

用于字符串和`python` 数据类型之间的转换，`JSON(JavaScript Object Notation)` 是一种轻量级的数据交换格式,在前后端传输数据中经常使用。

假如，我要传送一个字典出去，需要解决两个主要问题：

怎么表达这个字典成一个字符串？怎么把一个字符串，读回一个字典？

因此，我们需要一个标准化的，字符串表达方式，例如`JSON`，有点类似于，编码与解码。

基本接口：

```python
import json
di = {'a':1,1:2}
a = json.dumps(di)
#1.dumps(python对象)
#通常是，字典，元祖，列表，字符串，数字
#返回的是一个，JSON字符串

b = json.loads(a)
#2. loads(string)
#读取一个JSON字符串，如果满足格式标准，那么就会返回出如下四种之一
#字典，列表，字符串，数字

#3. dump(obj, file)
#dumps + open + write
 
#例：
import json

the_dict = {
	'a':123,
	'b':456
}
with open('json.txt', 'w') as f:
    json.dump(the_dict, f)

#4. load(file)
#loads + open + read
 
with open('json.txt','r') as f:
    print json.load(f)
```

Json主要应用于前后台的数据传输，在前台也有json格式的文件，前台可以把数据转成json格式的文件，传输到后台，后台再把json解析出来，再做相应处理。

#### `Pickle`

把变量从内存中变成可存储或传输的过程称之为序列化,也称之为对象的持久化保存

`pickle`实现`python`的`bytes`类型与`python`其他数据类型之间的转换。

```python
import pickle
di = {'a':1,'b':2}
#1.dumps(python对象)
#通常是，字典，元祖，列表，字符串，数字
#返回的是一个，bytes字符串

#2. loads(string)
#读取一个bytes字符串，如果满足格式标准，那么就会返回出如下四种之一
#字典，列表，字符串，数字

#3. dump(obj, file)
#dumps + open + write

#例：
import pickle

the_dict = {
	'a':123,
	'b':456
}
with open('pickle.txt', 'wb') as f:
    pickle.dump(the_dict, f)
    
#4. load(file)
#loads + open + read
 
with open('pickle.txt','rb') as f:
    xx = pickle.load(f)  
print(xxx)
```

在`python`内部，`json`和`pickle`是一样的，但是`pickle`是`python`才有的模块，所有一般情况下会比`json`要快一些，但是使用方法是一样的。

从空间和时间上说，`Pickle` 是可移植的。换句话说，`pickle` 文件格式独立于机器的体系结构，这意味着，例如，可以在 `Linux` 下创建一个 `pickle`，然后将它发送到在 `Windows` 或 `Mac OS` 下运行的 `Python` 程序。并且，当升级到更新版本的 `Python` 时，不必担心可能要废弃已有的 `pickle`。`Python` 开发人员已经保证 `pickle` 格式将可以向后兼容 `Python` 各个版本。



### 总结

`SQLALchemy`的学习就这么多，在工作中常用的也就是这些，大家要熟练两个地方，一个是写表的对应的类，即`module`；第二个是`query`。这两个是一定要会的。今天讲的多表查询和原生`SQL`的查询，也是常用的，需要多加练习。

`Json`和`Pickle`模块的使用很简单，使用过一次就知道，具体的应用在后面的学习中会逐步地体会到。






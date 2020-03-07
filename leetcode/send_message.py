# encoding:utf8

import pika

mq_name = 'guest'  # RabbitMQ的用户名
mq_pwd = 'guest'  # RabbitMQ的密码
mq_host = '127.0.0.1'  # RabbitMQ服务地址
mq_port = 5672  # RabbitMQ服务端口
mq_queue = 'queue_shao'  # 队列
mq_routing_key = 'queue_shao'  # 路由键
mq_body = "Hello World!"  # 生产者,发送的消息内容

# 身份验证凭证
credentials = pika.PlainCredentials(mq_name, mq_pwd)

# 创建连接
s_conn = pika.BlockingConnection(
    pika.ConnectionParameters(host=mq_host,
                              port=mq_port,
                              credentials=credentials))

# 在连接上创建一个频道
chan = s_conn.channel()

# 声明一个队列（生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行）
chan.queue_declare(queue=mq_queue)

# 发送消息
chan.basic_publish(exchange='', routing_key=mq_routing_key, body=mq_body)

for i in range(10):
    print("i-->", i)
    print("[生产者] send {0}".format(mq_body))

# 关闭连接（当生产者发送完消息后，可选择关闭连接）
s_conn.close()

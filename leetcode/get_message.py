import pika

mq_name = 'guest'  # RabbitMQ的用户名
mq_pwd = 'guest'  # RabbitMQ的密码
mq_host = '127.0.0.1'  # RabbitMQ服务地址
mq_port = 5672  # RabbitMQ服务端口
mq_queue = 'queue_shao'  # 队列

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


# 定义一个回调函数，用来接收生产者发送的消息
def callback(ch, method, properties, body):
    print("[消费者] recv {0}".format(body))


chan.basic_consume(on_message_callback=callback, queue=mq_queue, auto_ack=True)
# 取完一条消息后，不给生产者发送确认消息，默认是False的，
# 即默认给rabbitmq发送一个收到消息的确认，一般默认即可

print('[消费者] waiting for msg .')

# 开始循环取消息
chan.start_consuming()

import redis

host = "localhost"
port = "6379"
password = "OPen2019*"
r = redis.Redis(host=host, port=port, db=0, password=password)
n = 9999999
value = "AQWERRT8888888888888OOOOOOOOOOOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
while n > 0:
    r.set("key{0}".format(n), value)
    n -= 1

workers = 2
errorlog = "/demo/var/logs/mysite.gunicorn.error"
accesslog = "/demo/var/logs/mysite.gunicorn.access"
loglevel = "debug"

bind = ["127.0.0.1:9001"]

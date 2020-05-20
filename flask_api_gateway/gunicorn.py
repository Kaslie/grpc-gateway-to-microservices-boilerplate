import os

# worker_class = "eventlet"
threads = int(os.getenv("GUNICORN_THREADS", "1"))
workers = int(os.getenv("GUNICORN_TOTAL_WORKERS", "1"))
bind = "0.0.0.0:" + os.getenv("PORT", "5001")
timeout = 10800
syslog_addr = os.getenv("GUNICORN_SYSLOG_ADDRESS", "udp://")
syslog = True
loglevel = "info"
accesslog = "-"

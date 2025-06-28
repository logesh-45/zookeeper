import time
from kazoo.client import KazooClient
from kazoo.handlers.threading import KazooTimeoutError

def connect_to_zookeeper(max_retries=10, delay=2):
    for attempt in range(max_retries):
        try:
            zk = KazooClient(hosts="zk1:2181")
            zk.start(timeout=5)
            print("Connected to ZooKeeper.",flush=True)
            return zk
        except KazooTimeoutError:
            print(f"⏳ Attempt {attempt + 1}: ZooKeeper not ready, retrying in {delay}s...", flush=True)
            time.sleep(delay)
    print("Failed to connect to ZooKeeper after retries.", flush=True)
    exit(1)

zk = connect_to_zookeeper()
zk.ensure_path("/services/payment")
zk.create("/services/payment/instance1", b"http://payment-service:8080", ephemeral=True)

print("Service A registered as /services/payment/instance1 and holding session.",flush=True)
try:
    while True:
        time.sleep(10)  # Keep session alive
except KeyboardInterrupt:
    print("Shutting down Service A.",flush=True)
    zk.stop()


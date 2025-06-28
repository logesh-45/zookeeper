import time
from kazoo.client import KazooClient

zk = KazooClient(hosts="zk1:2181")
zk.start()

zk.ensure_path("/services/payment")

for _ in range(10):
    instances = zk.get_children("/services/payment")
    if instances:
        for inst in instances:
            data, _ = zk.get(f"/services/payment/{inst}")
            print("Connect to:", data.decode())
        break
    print("Waiting for payment service...", flush=True)
    time.sleep(2)
else:
    print("No payment service instances found after retries.", flush=True)

zk.stop()

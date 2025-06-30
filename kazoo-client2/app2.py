import time
from kazoo.client import KazooClient

zk = KazooClient(hosts="zk1:2181")
zk.start()
http=""
zk.ensure_path("/services/payment")

for _ in range(10):
    instances = zk.get_children("/services/payment")
    if instances:
        for inst in instances:
            data, _ = zk.get(f"/services/payment/{inst}")
            print("Connect to:", data.decode())
            http = data.decode()
        break
    print("Waiting for payment service...", flush=True)
    time.sleep(2)
else:
    print("No payment service instances found after retries.", flush=True)

zk.stop()



# import requests
# response = requests.get(f"https://{http}/api/payment/status")
# if response.status_code == 200:
#     print("Payment service response:", response.json())
# else:
#     print("Failed to connect to payment service:", response.status_code, response.text)
     
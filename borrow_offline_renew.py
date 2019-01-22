import requests
vray_next_node, vray_next_sdk = 15, 15
data = {"3888249":{"1":0,"2":vray_next_node,"4":0,"productId":3888249},"9779345":{"1":vray_next_sdk,"2":0,"4":0,"productId":9779345},"renew":True}
response = requests.post('http://127.0.0.1:30304/offline/reserve', json=data)
print(response.content)

#'http://172.21.232.203:5050/offline/release'
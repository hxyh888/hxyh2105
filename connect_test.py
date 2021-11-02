import random
import os
num_list = []
for i in range(4):
    num = str(random.randint(0,255))
    num_list.append(num)
    
ip = ".".join(num_list)
print(ip)
result = os.popen("ping %s"%ip)
print(result.read())
if "100%" in result.read():
    print("connect ok")
else:
    print("connect fail")



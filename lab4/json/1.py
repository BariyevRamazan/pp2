import json
with open("sample-data.json") as jf:
    a =json.load(jf)
n=int(input("from: "))
m=int(input("to: "))
print("Interface Status")
print("================================================================================")
print("DN",end="                                                 ")
print("Description           ",end="")
print("Speed    ",end="")
print("MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
dnp="-------------------------------------------------- "
desp="-------------------- "
spp="------  "
for i in range(n,m):
    dn=a["imdata"][i]["l1PhysIf"]["attributes"]['dn']
    des=a["imdata"][i]["l1PhysIf"]["attributes"]['descr']
    sp=a["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    mt=a["imdata"][i]["l1PhysIf"]["attributes"]['mtu']
    print(dn,end=(len(dnp)-len(dn))*" ")
    print(des,end=(len(desp)-len(des))*" ")
    print(sp,end=(len(spp)-len(sp))*" ")
    print(mt)
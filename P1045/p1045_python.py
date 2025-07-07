from math import log2

p = int(input())
print(int(p/log2(10))+1)

# Python comes with high precision

mei_num = pow(2,p,pow(10,500))-1
mei_num = 500*"0" + str(mei_num)

start = -500
end =  -450

for i in range(10):
    if i!=9:
        print(mei_num[start+50*i:end+50*i])
    else:
        print(mei_num[start+50*i:end+50*i-1]+mei_num[-1])
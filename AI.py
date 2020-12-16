# lil practice
import numpy as np
import matplotlib.pyplot as plt
# print('w1=%.2f'%w1,'w2=%.2f'%w2,'theta=%.2f'%theta)
# print('w1=%4.2f,w2=%4.2f'%(w1,w2))

#initial


w1=0.2
w2=0.3
y=[]
yd=[0,1,1,1]
theta=0.7
alpha=0.2
p=np.arange(0,3,0.01)
wa1=[]
wa2=[]

#函數
def linear(A):
    return (theta-A*w1)/w2
#input
choice=int(input("請選擇執行邏輯:輸入1為and,2為or:"))
if choice == 1 :
    yd=[0,0,0,1]
else:
    yd=[0,1,1,1]
    
w1=float(input('輸入w1值:'))
print('你設定的w1值是:',w1)

w2=float(input('輸入w2值:'))
print('你設定的w2值是:',w2)

theta=float(input('輸入theta值:'))
print('你設定的theta值是:',theta)


plt.axis([0,2,0,2])
plt.plot([0,0],'ro',[0,1],'ro',[1,0],'ro',[1,1],'ro')

z=linear(p)
plt.plot(p,z)
plt.show()


# 迴圈
for x1 in range(2):
    for x2 in range(2):
        ya=((x1*w1+x2*w2)-theta)
        if ya > 0 :
            y.append(1)  
        else:
            y.append(0)
                 
print(y)       
y=np.array(y)

yd=np.array(yd) 
print(yd)      
e=(yd-y)
print(e)

while (e[0] or e[1] or e[2] or e[3] !=0) :
    for i in range(4) :
        if (e[i] != 0) :
           for x1 in range(2):
               for x2 in range(2):
                   if x1 == 0:
                      w2=w2+(alpha*x2*e[i])
                      w1=w1
                      plt.axis([0,2,0,2])
                      plt.plot([0,0],'ro',[0,1],'ro',[1,0],'ro',[1,1],'ro')
                      z=linear(p)
                      plt.plot(p,z)
                      plt.show()
                      
                      if (x1*w1+x2*w2)-theta >= 0:
                          e[i] = 0
                          wa1.append(w1)
                          wa2.append(w2)
                      else:
                          wa1.append(w1)
                          wa2.append(w2)
                   
                   elif x2 == 0:
                      w1=w1+(alpha*x1*e[i])
                      w2=w2
                      plt.axis([0,2,0,2])
                      plt.plot([0,0],'ro',[0,1],'ro',[1,0],'ro',[1,1],'ro')
                      z=linear(p)
                      plt.plot(p,z)
                      plt.show()
                      
                      if (x1*w1+x2*w2)-theta >= 0:
                          e[i] = 0
                          wa1.append(w1)
                          wa2.append(w2)
                      else:
                          wa1.append(w1)
                          wa2.append(w2)
                      
                      
        else:
            pass


wa1=np.array(wa1)            
wa2=np.array(wa2)           
            
            
print(wa1)
print(wa2)









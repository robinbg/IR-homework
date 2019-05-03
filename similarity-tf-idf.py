import os
test_tf=dict()
doc_sum=dict()
with open("obj.txt","r") as f:
    st=f.read()
    
    for s in st.split():
        s1=s.lower()
        doc_sum[s1]=1
        if s1 in test_tf:
            test_tf[s1]+=1
        else:
            test_tf[s1]=1
tfs=[]
for i in range(1,4):
    with open("./collection/"+str(i)+".txt","r") as f1:
        st=f1.read()
        tf=dict()
        for s in st.split():
            s1=s.lower()
           
            if s1 in tf:
                tf[s1]+=1
              
            else:
                tf[s1]=1
                if s1 in doc_sum:
                    doc_sum[s1]+=1
                else:
                    doc_sum[s1]=1
        tfs.append(tf)
 from math import log

arr=[]
for s in doc_sum.keys():
    if s in test_tf:
        arr.append((1+test_tf[s])*log(4/doc_sum[s]))
    else:
        arr.append(log(4/doc_sum[s]))
import numpy as np
vec_obj=np.array(arr)
len_obj=np.dot(vec_obj,vec_obj)

from queue import PriorityQueue
Q=PriorityQueue()
for i in range(3):
    arr=[]
    for s in doc_sum.keys():
        if s in tfs[i]:
            arr.append((1+tfs[i][s])*log(4/doc_sum[s]))
        else:
            arr.append(log(4/doc_sum[s]))
    vec=np.array(arr)
    print(vec)
    len_vec=np.dot(vec,vec)
    pro=np.dot(vec,vec_obj)
    if pro!=0:
        Q.put((-1.0*pro*pro/len_vec/len_obj,i+1))
    else:
        Q.put((0,i+1))

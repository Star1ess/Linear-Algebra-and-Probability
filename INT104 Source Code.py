import csv
import numpy as np
from collections import Counter
csv_file = open('binary_data.csv' )
csv_reader = csv.reader(csv_file, delimiter=',')
final_list = list(csv_reader)
matrix = np.array(final_list)


# Read the text ﬁle and parse its content into a matrix. (20 scores)
print(matrix)


# Compute the prior probabilities p(l = 0) and p(l = 1) (20 scores)



#a0 = matrix[:, 0]
#a1 = matrix[:, 1]
#a2 = matrix[:, 2]
#a3 = matrix[:, 3]
#a4 = matrix[:, 4]
l = matrix[:, 5]

ai0 = matrix[:, [0, 5]]
ai1 = matrix[:, [1, 5]]
ai2 = matrix[:, [2, 5]]
ai3 = matrix[:, [3, 5]]
ai4 = matrix[:, [4, 5]]

q1 = np.array(['0', '0'])
q2 = np.array(['1', '0'])
q3 = np.array(['0', '1'])
q4 = np.array(['1', '1'])


N: int = len(matrix)
#print(N)

l0 = Counter(l)['0']
p1 = l0/N
print(p1)

l1 = Counter(l)['1']
p2 = l1/N
print(p2)



#3

##1


p3 = (ai0 == q1).all(1).sum()/l0
print(p3)

p4 = (ai1 == q1).all(1).sum()/l0
print(p4)

p5 = (ai2 == q1).all(1).sum()/l0
print(p5)

p6 = (ai3 == q1).all(1).sum()/l0
print(p6)

p7 = (ai4 == q1).all(1).sum()/l0
print(p7)


##2
p8 = (ai0 == q2).all(1).sum()/l0
print(p8)

p9 = (ai1 == q2).all(1).sum()/l0
print(p9)

p10 = (ai2 == q2).all(1).sum()/l0
print(p10)

p11 = (ai3 == q2).all(1).sum()/l0
print(p11)

p12 = (ai4 == q2).all(1).sum()/l0
print(p12)

##3
p13 = (ai0 == q3).all(1).sum()/l1
print(p13)

p14 = (ai1 == q3).all(1).sum()/l1
print(p14)

p15 = (ai2 == q3).all(1).sum()/l1
print(p15)

p16 = (ai3 == q3).all(1).sum()/l1
print(p16)

p17 = (ai4 == q3).all(1).sum()/l1
print(p17)

##4
p18 = (ai0 == q4).all(1).sum()/l1
print(p18)

p19 = (ai1 == q4).all(1).sum()/l1
print(p19)

p20 = (ai2 == q4).all(1).sum()/l1
print(p20)

p21 = (ai3 == q4).all(1).sum()/l1
print(p21)

p22 = (ai4 == q4).all(1).sum()/l1
print(p22)
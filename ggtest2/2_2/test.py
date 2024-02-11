import numpy as np 
import sol1
import sol2
import sol_teryn


randints = [np.random.randint(1, 100) for i in range(1000)]
teryns = randints[:]
mine = randints[:]
sol2mine= randints[:]
t = 305

print(sol1.solution(teryns, t))
print(sol_teryn.solution(mine, t))
print(sol2.solution(sol2mine, t))
# print(ran:dints)

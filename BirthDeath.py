import random, math
tmax = 100
x0 = 10
t = 0
x = x0
while t <= tmax:
    lamb = 1
    mu = 2
    if x==0:
        mu = 0
        rate = lamb+mu
        urv = random.random()
        if urv >= lamb/rate:
            x -= 1
        else:
            x +=1
            t += -math.log(random.random())/rate

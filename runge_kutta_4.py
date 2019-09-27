import matplotlib.pyplot as plt


class RungeKutta4():
    def __init__(self, h):
        def phi(x, y, f, s, i):
            f_1 = h * f(x,y,s,i)
            f_2 = h * f(x + h/2, y + f_1/2, s, i)
            f_3 = h * f(x + h/2, y + f_2/2, s, i)
            f_4 = h * f(x + h/2, y + f_3, s, i)
            return y + 1/6 * (f_1 + 2*f_2 + 2*f_3 + f_4)
        self.phi = phi

    def eval(self, s, i, r, t, beta, v):

        def f_s(x,y,s,i):
            return -beta*y*i

        def f_i(x,y,s,i):
            return beta*s*y - v*y

        def f_r(x,y,s,i):
            return v*i

        return self.phi(t,s,f_s,s,i), self.phi(t,i,f_i,s,i), self.phi(t,r,f_r,s,i)

s = [1500]
i = [1]
r = [0]
tot = [1501]

rk4 = RungeKutta4(0.5)

for t in range(1, 61):
    s_t, i_t, r_t = rk4.eval(s[t-1],i[t-1],r[t-1],1,0.0005,0.1)
    print(s_t, i_t, r_t)
    s.append(s_t)
    i.append(i_t)
    r.append(r_t)
    tot.append(s_t+i_t+r_t)

t = range(0, 61)

plt.plot(t, s)
plt.plot(t, i)
plt.plot(t, r)
plt.plot(t, tot)

plt.show()
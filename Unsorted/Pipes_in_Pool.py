pool_v = int(input())
deb_pipe_1 = int(input())
deb_pipe_2 = int(input())
time_gone = float(input())

l_pipe_1 = deb_pipe_1 * time_gone
l_pipe_2 = deb_pipe_2 * time_gone

sum_litres = l_pipe_1 + l_pipe_2
pool_l = (sum_litres / pool_v) * 100

perc_pipe_1 = (l_pipe_1 / sum_litres) * 100
perc_pipe_2 = (l_pipe_2 / sum_litres) * 100

if pool_l <= pool_v:
    print(f"The pool is {pool_l:.2f}% full. Pipe 1: {perc_pipe_1:.2f}%. Pipe 2: {perc_pipe_2:.2f}%.")
else:
    print(f"For {time_gone:.2f} hours the pool overflows with {(pool_l - pool_v):.2f} liters.")

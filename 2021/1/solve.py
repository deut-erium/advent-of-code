with open('input.txt','r') as f:
    data = list(map(int, f.read().strip().split()))

num_increased = sum(j>i for i,j in zip(data,data[1:]))
print(num_increased)

WINDOW_SIZE = 3
num_win_increased = sum(sum(win[1:])>sum(win[:-1]) for win in  zip(*[data[i:] for i in range(WINDOW_SIZE+1)]))

print(num_win_increased)

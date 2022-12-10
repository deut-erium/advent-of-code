with open("input", "r") as f:
    forest = [list(map(int,list(x))) for x in f.read().strip().split()]


assert len(forest)==len(forest[0])
n = len(forest)

visible = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    visible[i][0] = True
    visible[0][i] = True
    visible[-1][i] = True
    visible[i][-1] = True
    h_left, h_right, h_top, h_bot = 0,0,0,0
    for j in range(n):
        if (curr:=forest[i][j])>h_left:
            visible[i][j] = True
            h_left = curr
        if (curr:=forest[i][~j])>h_right:
            visible[i][~j] = True
            h_right = curr
        if (curr:=forest[j][i])>h_top:
            visible[j][i] = True
            h_top = curr
        if (curr:=forest[~j][i])>h_bot:
            visible[~j][i] = True
            h_bot = curr


print(sum(map(sum,visible)))

scenic = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    scenic[i][0]  = 0
    scenic[0][i]  = 0
    scenic[-1][i] = 0
    scenic[i][-1] = 0

for i in range(n):
    for j in range(n):
        k = j-1
        while k>0 and forest[i][j]>forest[i][k]:
            k-=1
        scenic[i][j]*=j-k

        k = j-1
        while k>0 and forest[i][~j]>forest[i][~k]:
            k-=1
        scenic[i][~j]*=j-k

        k = j-1
        while k>0 and forest[j][i]>forest[k][i]:
            k-=1
        scenic[j][i]*=j-k

        k = j-1
        while k>0 and forest[~j][i]>forest[~k][i]:
            k-=1
        scenic[~j][i]*=j-k


print(max(map(max,scenic)))

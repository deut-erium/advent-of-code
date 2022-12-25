with open("input") as f:
    data = f.read()

# data = """1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122"""

SNAFU = {
         "2":2,
         "1":1,
         "0":0,
         "-":-1,
         "=":-2
        }
REV_SNAFU = {
        2:"2",
        1:"1",
        0:"0",
        -1:"-",
        -2:"="
        }

def snafu_to_dec(num_str):
    res = 0
    pow = 1
    for i in num_str[::-1]:
        res+=SNAFU[i]*pow
        pow*=5
    return res

def dec_to_snafu(num):
    res = []
    while num:
        num,rem = divmod(num, 5)
        if rem>=3:
            num+=1
            rem-=5
        res.append(rem)
    return "".join(REV_SNAFU[i] for i in res[::-1])


print(dec_to_snafu(sum(map(snafu_to_dec,data.split()))))

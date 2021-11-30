with open('input.txt','r') as f:
    passes = f.read().strip().split()

TRANS = "".maketrans({'F':'0','B':'1','L':'0','R':'1'})

def get_pass_no(boarding_pass):
    return int(boarding_pass.translate(TRANS),2)

passes = list(map(get_pass_no,passes))
max_pass = max(passes)
print(max_pass)

print(set(range(max_pass-len(passes),max_pass+1))-set(passes))



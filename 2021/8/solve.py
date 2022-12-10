with open('input.txt') as f:
    data = f.read().strip().split('\n')
    inputs, outputs = [],[]
    for line in data:
        inp, oup = line.split(' | ')
        inputs.append(inp.strip().split())
        outputs.append(oup.strip().split())
        
inp_digits = [[sorted(ord(i)-ord('a') for i in c) for c in inp] for inp in inputs]
oup_digits = [[sorted(ord(i)-ord('a') for i in c) for c in oup] for oup in outputs]



from itertools import permutations
DIGIT_MAPS = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
DIGIT_MAPS_INTS = [ [ord(i)-ord('a') for i in dig] for dig in DIGIT_MAPS]
DIG_LENS = [len(i) for i in DIGIT_MAPS]

def find_possible_decodings(inp,oup):
    decodings = []
    for mapping in permutations(range(7)):
        correct_map = True
        for i in inp:
            if sorted([mapping[j] for j in i]) not in DIGIT_MAPS_INTS:
                correct_map = False
                break
        if correct_map:
            output = []
            for o in oup:
                out_dig = DIGIT_MAPS_INTS.index(sorted([mapping[j] for j in o]))
                output.append(out_dig)
            return output
            # decodings.append(output)
    # return decodings

num_outputs = sum(sum(len(i) in [DIG_LENS[i] for i in [1,4,7,8]] for i in oup) for oup in outputs)
print(num_outputs)

output_decoded = []

for inp,oup in zip(inp_digits,oup_digits):
    digits =  find_possible_decodings(inp,oup)
    num = int("".join(map(str,digits)))
    output_decoded.append(num)
   
print(sum(output_decoded))

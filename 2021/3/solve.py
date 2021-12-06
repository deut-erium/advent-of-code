from collections import Counter
with open('input.txt') as f:
    data = f.read().strip().split()

bit_width = len(data[0])
pos_counter = [Counter() for _ in range(bit_width)]
for dig_repo in data:
    for c,bit in zip(pos_counter, dig_repo):
        c[bit]+=1

highs = [c.most_common(1)[0][0] for c in pos_counter]
gamma = int("".join(highs),2)
epsilon = (2**bit_width) -1 - gamma
print(gamma*epsilon)



O2_gen_rating, CO2_scrub_rating = data.copy(), data.copy()
for i in range(bit_width):
    O2_set_one, O2_set_zero, zero_maj_o2 = [],[],0
    for dig_repo in O2_gen_rating:
        if dig_repo[i]=='1':
            O2_set_one.append(dig_repo)
            zero_maj_o2 -=1
        else:
            O2_set_zero.append(dig_repo)
            zero_maj_o2 +=1
    O2_gen_rating = O2_set_zero if zero_maj_o2>0 else O2_set_one
    if len(O2_gen_rating)==1:
        break

for i in range(bit_width):
    CO2_set_one, CO2_set_zero, one_maj_co2 = [], [],0
    for dig_repo in CO2_scrub_rating:
        if dig_repo[i]=='1':
            CO2_set_one.append(dig_repo)
            one_maj_co2 +=1
        else:
            CO2_set_zero.append(dig_repo)
            one_maj_co2 -=1
    CO2_scrub_rating = CO2_set_zero if one_maj_co2>=0 else CO2_set_one
    if len(CO2_scrub_rating)==1:
        break

print(int(O2_gen_rating[0],2)*int(CO2_scrub_rating[0],2))

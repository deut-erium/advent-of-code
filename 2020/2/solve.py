with open('input.txt','r') as f:
    data = f.read().strip().split('\n')

from collections import Counter
def validate_pw_token(token):
    rule, passw = token.split(': ')
    count_range, rule_char = rule.split()
    count_low, count_high = map(int, count_range.split('-'))
    char_counter = Counter(passw)
    return count_low <= char_counter[rule_char] <= count_high


def validate_pw_token2(token):
    rule, passw = token.split(': ')
    pos_range, rule_char = rule.split()
    pos_low, pos_high = map(int, pos_range.split('-'))
    return (passw[pos_low-1]==rule_char)^(passw[pos_high-1]==rule_char)

print(sum(map(validate_pw_token,data)))
print(sum(map(validate_pw_token2,data)))
    


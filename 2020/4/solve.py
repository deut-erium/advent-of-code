with open('input.txt','r') as f:
    passports = f.read().strip().split('\n\n')

REQUIRED_FIELDS = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

def validate_passport(token):
    fields = {i.split(':')[0] for i in token.strip().split()}
    return all(field in fields for field in REQUIRED_FIELDS)

print(sum(map(validate_passport,passports)))

def val_byr(byr):
    try:
        return 1920 <= int(byr) <= 2002
    except:
        return False

def val_iyr(iyr):
    try:
        return 2010 <= int(iyr) <= 2020
    except:
        return False

def val_eyr(eyr):
    try:
        return 2020 <= int(eyr) <= 2030
    except:
        return False

def val_hgt(hgt):
    try:
        if hgt.endswith('cm'):
            return 150 <= int(hgt[:-2]) <= 193
        elif hgt.endswith('in'):
            return 59 <= int(hgt[:-2]) <= 76
        return False
    except:
        return False

def val_hcl(hcl):
    hexa = '0123456789abcdef'
    return len(hcl)==7 and hcl[0]=='#' and all(i in hexa for i in hcl[1:])

def val_ecl(ecl):
    return ecl in {'amb','blu','brn','gry','grn','hzl','oth'}

def val_pid(pid):
    dig = '0987654321'
    try:
        return len(pid)==9 and all(i in dig for i in pid)
    except:
        return False

validators = {
        'byr':val_byr,
        'iyr':val_iyr,
        'eyr':val_eyr,
        'hgt':val_hgt,
        'hcl':val_hcl,
        'ecl':val_ecl,
        'pid':val_pid,
        'cid':lambda x:True
        }

def validate_passport2(tokens):
    token_dict = {}
    for token in tokens.split():
        typ,val = token.split(":")
        token_dict[typ]=val
        # print(typ, validators[typ](val))
    return all(tok in token_dict for tok in REQUIRED_FIELDS) \
        and all(validators[typ](val) for typ,val in token_dict.items())


print(sum(map(validate_passport2,passports)))


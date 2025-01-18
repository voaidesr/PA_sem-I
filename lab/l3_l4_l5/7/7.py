def unify(dict1, dict2):
    dict_rez = {}
    for k in dict1:
        if k not in dict2:
            dict_rez[k] = dict1[k]
        else:
            dict_rez[k] = dict1[k] + dict2[k]
    for k in dict2:
        if k not in dict1:
            dict_rez[k] = dict2[k]
    return dict_rez

def unify1(dict1, dict2):
    keys = set(dict1.keys()).union(set(dict2.keys()))
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in keys}

from collections import Counter

def unify2(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

from collections import defaultdict

def unify3(dict1, dict2):
    dict_rez = defaultdict(int)
    for k, v in dict1.items():
        dict_rez[k] += v
    for k, v in dict2.items():
        dict_rez[k] += v
    return dict(dict_rez)

def unify4(dict1, dict2):
    dict_rez = {}
    for k, v in dict1.items():
        dict_rez[k] = dict_rez.setdefault(k, 0) + v
    for k, v in dict2.items():
        dict_rez[k] = dict_rez.setdefault(k, 0) + v
    return dict_rez

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    
    result = unify(dict1, dict2)
    print("Result using original unify:", result)
    
    result1 = unify1(dict1, dict2)
    print("Result using unify1:", result1)
    
    result2 = unify2(dict1, dict2)
    print("Result using unify2:", result2)
    
    result3 = unify3(dict1, dict2)
    print("Result using unify3:", result3)
    
    result4 = unify4(dict1, dict2)
    print("Result using unify4:", result4)

if __name__ == "__main__":
    main()
def division(a, b):
    return a/b


def parity(a):
    if a % 2 == 0:
        return True


def rounded(a):
    if a-a//1==0:
        return True
    else: return False

def size_less_a(dict_sample,a):
    if len(dict_sample)<a:
        return True
def first_int(dict_sample,key):
    if type(dict_sample[key])==int:
        return True

def size_more_a(dict_sample,a):
    if len(dict_sample)>a:
        return True
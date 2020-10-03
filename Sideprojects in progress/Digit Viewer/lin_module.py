e = 2.7182818284590452353602874713526624977572470936999595749669676

def add_vec(a,b):
    output = None
    if len(a) == len(b):
        output = [a[i] + b[i] for i in range(len(a))]
        return output
    else:
        raise Exception("Input vectors different length")

def sub_vec(a,b):
    output = None
    if len(a) == len(b):
        output = [a[i] - b[i] for i in range(len(a))]
        return output
    else:
        raise Exception("Input vectors different length")

def mult_vec(a,b):
    output = None
    if len(a) == len(b):
        output = [a[i] * b[i] for i in range(len(a))]
        return output
    else:
        raise Exception("Input vectors different length")

def scale(s,v):
    output = [s*v[i] for i in range(len(v))]
    return output

def matrix_mult(M,v):
    if len(M) == len(v):
        temp = [scale(v[i],M[i]) for i in range(len(v))]
        output = [0 for _ in range(len(temp[0]))]
        for x in temp:
            output = add_vec(output,x)
        return output
    else:
        raise Exception(M, v)

def transpose(M):
    output = []
    for x in range(len(M[0])):
        temp = []
        for y in range(len(M)):
            temp.append(M[y][x])
        output.append(temp)

    return output

def sigmoid(v):
    output = []
    for x in v:
        try:
            output.append(1/(1+e**(-x)))
        except OverflowError:
            if x > 0:
                output.append(1)
            else:
                output.append(0)
    return output

def d_sigmoid(v):
    output = []
    for s in v:
        try:
            output.append((e**(-s)/((1+e**(-s))**2)))
        except OverflowError:
            output.append(0)
    return output
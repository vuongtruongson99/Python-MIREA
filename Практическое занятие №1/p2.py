def f21(lst):
    if lst[1] == 'lfe':
        if lst[2] == 1994:
            if lst[3] == 1959:
                return 0
            elif lst[3] == 1993:
                return 1
            elif lst[3] == 1965:
                return 2
        elif lst[2] == 1998:
            if lst[3] == 1959:
                return 3
            elif lst[3] == 1993:
                return 4
            elif lst[3] == 1965:
                return 5
        elif lst[2] == 2010:
            return 6
    elif lst[1] == 'cobol':
        if lst[0] == 1998:
            return 7
        elif lst[0] == 1989:
            return 8
        elif lst[0] == 1975:
            if lst[2] == 1994:
                return 9
            elif lst[2] == 1998:
                return 10
            elif lst[2] == 2010:
                return 11

def f22(x):
    A = int(x) & 0b00000000000000000000000000000111
    B = (int(x) >> 3) & 0b00000000000000000000000000111
    C = (int(x) >> 6) & 0b00000000000000000001111111
    D = (int(x) >> 13) & 0b0000000000011111111
    E = (int(x) >> 21) & 0b00000011111
    F = (int(x) >> 26) & 0b000001
    G = (int(x) >> 27) & 0b00011
    H = (int(x) >> 29) 

    ans = (E << 27) + (B << 24) + (G << 22) + (A << 19) + (D << 11) + (H << 8) + (C << 1) + F
    return ans    

    
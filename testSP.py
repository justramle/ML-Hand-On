def add(x,y):
    return x + y

def test_add():
    assert add(1,3) == 4

def test_add_strings():
    assert add("concate","worcsds") == ("concatewords")

def parse(s):
    assert type(s) is str 
    assert len(s) >= 1
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    assert len(s) >=1
    n = 0
    for c in s:
        n = n*10 + ord(s) - ord('0')
    return n * sign
    

def test_parse_zero():
    # assert parse("0") == 0
    # assert parse("1") == 1
    k = 0
    for c  in "0123456789":
        assert parse(c) == k, f"string {[c]} does not parses as {[k]}"
        k = k+1
    return k

def test_parse_single_digit():
    k = 0
    for c  in "0123456789":
        assert parse(c) == k, f"string {[c]} does not parses as {[k]}"
        k = k+1
    return k

def test_parse_multiple_digit():
    assert parse("22") == 22

def test_parse_negative_digit():
    assert parse("-22") == 22


if __name__ == "__main__":
    test_parse_multiple_digit()
    test_parse_zero()
    test_parse_negative_digit()
    print("done.")
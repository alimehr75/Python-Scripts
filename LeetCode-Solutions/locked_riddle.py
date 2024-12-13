def check_nums(a: str, b: str) -> tuple:
    correct, found = 0, 0
    for i, j in zip(a, b):
        if i == j:
            a = a.replace(i, "")
            b = b.replace(j, "")
            correct += 1

    for c in a:
        if c in b:
            found += 1
            b.replace(c,"")

    return correct, found

for i in range(1000):
    i = str(i).zfill(3)
    if check_nums(i,"682") == (1,0) and \
       check_nums(i,"614") == (0,1) and \
       check_nums(i,"206") == (0,2) and \
       check_nums(i,"738") == (0,0) and \
       check_nums(i,"380") == (0,1):
        print(i)


       
def test_sit():
    assert check_nums("123","124") == (2,0)
    assert check_nums("123","142") == (1,1)
    assert check_nums("123","123") == (3,0)
    assert check_nums("123","456") == (0,0)


count = 0
range = range(1, 51)
nmb_output = 15


nmb_output -= 1
tmp = 4
for a in range:
    for b in range:
        napiv = a**3 + b**3
        for c in range:
            for d in range:
                if napiv == c**3 + d**3 and a not in (b, c, d) and b not in (c, d) and c!=d:
                    if tmp%4==0:
                        print("a =", a, "b =", b, "\t|", "c =", c, "d =", d, " \t*", napiv)
                        count += 1
                    tmp += 1
                if count > nmb_output:
                    break
            if count > nmb_output:
                break
        if count > nmb_output:
            break
    if count > nmb_output:
        break

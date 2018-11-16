g1 = 6
g2 = 4
g3 = 5

total = 70
count = 0

for lowrange in range(0, int(total / g1) + 2):
    for midrange in range(0, int(total / g2) + 2):
        for highrange in range(0, int(total / g3) + 2):
            if lowrange * g1 + midrange * g2 + highrange * g3 == total and lowrange != 0 and midrange != 0 and highrange != 0:
                count += 1
                print("Numbers: " + str(lowrange), "x", int(g1), ",", str(midrange), "x", int(g2), ",", str(highrange)
                      , "x", int(g3), "=", lowrange * g1 + midrange * g2 + highrange * g3)

print("Total combinations: ", count)

def decryptRailFence(cipher, key):
    rail = [["\n" for _ in cipher] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for pos, _ in enumerate(cipher):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = "*"
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j, _ in enumerate(cipher):
            if rail[i][j] == "*":
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for _ in cipher:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        result.append(rail[row][col])
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


if __name__ == "__main__":
    print(
        decryptRailFence(
            r"I_a__rgtcl_a_nArl_n_h_lcswr_tiigtite.twsabih_oddyi_pi,adtecok_eesrkn_hren",
            2,
        )
    )

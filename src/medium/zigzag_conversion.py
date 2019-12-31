def convert(s: str, numRows: int):
    agg = []
    for row in range(0, numRows):
        for start_idx in range(0, len(s), max(2 * numRows - 2, 1)):
            if row == 0:
                agg.append(s[start_idx])
            elif row == numRows - 1 and start_idx + numRows - 1 < len(s):
                agg.append(s[start_idx + numRows - 1])
            else:
                if start_idx + row < len(s):
                    agg.append(s[start_idx + row])
                    next_index = start_idx + 2 * numRows - 2 - row
                    if next_index < len(s):
                        agg.append(s[next_index])

    return "".join(agg)


print(convert("PAYPALISHIRING", 4))

def compress(s: str) -> str:
    if s == "":
        return ""

    for ind, _ in enumerate(s):
        if ind == 0:
            # if it's the first char initialize output with it
            output = s[0]
            count = 1
        else:
            if s[ind] == s[ind - 1]:
                count += 1
                if ind + 1 == len(s):
                    output += str(count)
            else:
                # append number of occurrences and next char
                output += str(count) + s[ind]
                count = 1
                if ind + 1 == len(s):
                    output += str(count)
    return output

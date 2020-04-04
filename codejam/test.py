def solution(s):
    nested_s = ""
    s = "0" + s + "0"

    for i in range(1, len(s)-1):
        nested_s += "(" * (int(s[i]) - int(s[i-1]) if int(s[i]) > int(s[i-1]) else 0) + s[i] \
                    + ")" * (int(s[i]) - int(s[i+1]) if int(s[i]) > int(s[i+1]) else 0)

    return nested_s


print(solution("1111000"))
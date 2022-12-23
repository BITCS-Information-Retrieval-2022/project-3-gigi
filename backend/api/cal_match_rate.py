
def remove_fuhao(s1):
    s1 = s1.replace(",", " ")
    s1 = s1.replace(".", " ")
    s1 = s1.replace(":", " ")
    s1 = s1.replace("\"", " ")
    s1 = s1.replace("!", " ")
    s1 = s1.replace("?", " ")
    s1 = s1.replace("-", " ")
    s1 = s1.lower()
    return s1


def cal_match_rate(s1, s2):
    s1 = remove_fuhao(s1)
    s2 = remove_fuhao(s2)
    print(s1)
    print(s2)
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    print(s1)
    print(s2)
    s2_dict = {}
    for i in range(len(s2)):
        if s2[i] in s2_dict.keys():
            s2_dict[s2[i]] += 1
        else:
            s2_dict[s2[i]] = 1
    cnt = 0
    for i in range(len(s1)):
        if s1[i] in s2_dict.keys() and s2_dict[s1[i]] != 0:
            cnt += 1
            s2_dict[s1[i]] -= 1
    print(cnt / len(s1))
    if cnt / len(s1) >= 0.5:
        return 1
    else:
        return 0


if __name__ == '__main__':
    s1 = "Deep Learning for Content-Based Image Retrieval: A Comprehensive Study"
    s2 = "Deep Learning - 014  Content based image retrieval"
    print(cal_match_rate(s1, s2))

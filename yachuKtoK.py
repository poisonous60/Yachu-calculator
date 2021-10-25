import numpy as np

#input
# H : numpy (6) array, [1짜리 킵 개수, 2짜리 킵 개수, ..., 6짜리 킵 개수], 현재 킵한 상태
# 예를 들어 1짜리 2개 킵했으면 [2,0,0,0,0,0]
#
# output:
# G : numpy (6^5) array, [1짜리 킵 개수, 2짜리 킵 개수, ..., 6짜리 킵 개수], 현재 킵에서 다음 나올 킵의 경우의 수
# 예를 들어 1짜리 2개, 2짜리 3개 킵한 경우의 수는 G[2][3][0][0][0][0]
#
def KtoK(H):
    sumH=H.sum()
    if(sumH < 0 or sumH > 5):
        print("주사위 개수 이상함")
        print("H: %s" %H)
        return -1
    number_of_roll_dice = 5-H.sum()
    if(number_of_roll_dice < 0 or number_of_roll_dice > 5):
        print("주사위 개수 이상함")
        print("H: %s" %H)
        print("number_of_roll_dice : %d" %number_of_roll_dice)
        return -1
    else:
        pass

    filter = []
    for i in range(5):
        if number_of_roll_dice > 0:
            filter.append(True)
            number_of_roll_dice = number_of_roll_dice - 1
        else:
            filter.append(False)
    number_of_roll_dice = 5-H.sum()

    G = np.zeros(shape=(6,6,6,6,6,6))

    
    if number_of_roll_dice == 5:
        for d1 in range(1,7):
            for d2 in range(1,7):
                for d3 in range(1,7):
                    for d4 in range(1,7):
                        for d5 in range(1,7):
                            D = np.array([d1, d2, d3, d4, d5])
                            D = list(D)
                            i1 = int(D.count(1) + H[0])
                            i2 = int(D.count(2) + H[1])
                            i3 = int(D.count(3) + H[2])
                            i4 = int(D.count(4) + H[3])
                            i5 = int(D.count(5) + H[4])
                            i6 = int(D.count(6) + H[5])
                            for ii1 in range(0, i1+1):
                                for ii2 in range(0, i2+1):
                                    for ii3 in range(0, i3+1):
                                        for ii4 in range(0, i4+1):
                                            for ii5 in range(0, i5+1):
                                                for ii6 in range(0, i6+1):
                                                    G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    elif number_of_roll_dice == 4:
        for d1 in range(1,7):
            for d2 in range(1,7):
                for d3 in range(1,7):
                    for d4 in range(1,7):
                        D = np.array([d1, d2, d3, d4])
                        D = list(D)
                        i1 = int(D.count(1) + H[0])
                        i2 = int(D.count(2) + H[1])
                        i3 = int(D.count(3) + H[2])
                        i4 = int(D.count(4) + H[3])
                        i5 = int(D.count(5) + H[4])
                        i6 = int(D.count(6) + H[5])
                        for ii1 in range(0, i1+1):
                            for ii2 in range(0, i2+1):
                                for ii3 in range(0, i3+1):
                                    for ii4 in range(0, i4+1):
                                        for ii5 in range(0, i5+1):
                                            for ii6 in range(0, i6+1):
                                                G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    elif number_of_roll_dice == 3:
        for d1 in range(1,7):
                for d2 in range(1,7):
                    for d3 in range(1,7):
                        D = np.array([d1, d2, d3])
                        D = list(D)
                        i1 = int(D.count(1) + H[0])
                        i2 = int(D.count(2) + H[1])
                        i3 = int(D.count(3) + H[2])
                        i4 = int(D.count(4) + H[3])
                        i5 = int(D.count(5) + H[4])
                        i6 = int(D.count(6) + H[5])
                        for ii1 in range(0, i1+1):
                            for ii2 in range(0, i2+1):
                                for ii3 in range(0, i3+1):
                                    for ii4 in range(0, i4+1):
                                        for ii5 in range(0, i5+1):
                                            for ii6 in range(0, i6+1):
                                                G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    elif number_of_roll_dice == 2:
        for d1 in range(1,7):
            for d2 in range(1,7):
                D = np.array([d1, d2])
                D = list(D)
                i1 = int(D.count(1) + H[0])
                i2 = int(D.count(2) + H[1])
                i3 = int(D.count(3) + H[2])
                i4 = int(D.count(4) + H[3])
                i5 = int(D.count(5) + H[4])
                i6 = int(D.count(6) + H[5])
                for ii1 in range(0, i1+1):
                    for ii2 in range(0, i2+1):
                        for ii3 in range(0, i3+1):
                            for ii4 in range(0, i4+1):
                                for ii5 in range(0, i5+1):
                                    for ii6 in range(0, i6+1):
                                        G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    elif number_of_roll_dice == 1:
        for d1 in range(1,7):
            D = np.array([d1])
            D = list(D)
            i1 = int(D.count(1) + H[0])
            i2 = int(D.count(2) + H[1])
            i3 = int(D.count(3) + H[2])
            i4 = int(D.count(4) + H[3])
            i5 = int(D.count(5) + H[4])
            i6 = int(D.count(6) + H[5])
            for ii1 in range(0, i1+1):
                for ii2 in range(0, i2+1):
                    for ii3 in range(0, i3+1):
                        for ii4 in range(0, i4+1):
                            for ii5 in range(0, i5+1):
                                for ii6 in range(0, i6+1):
                                    G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    elif number_of_roll_dice == 0:
        i1 = H[0]
        i2 = H[1]
        i3 = H[2]
        i4 = H[3]
        i5 = H[4]
        i6 = H[5]
        for ii1 in range(0, i1+1):
            for ii2 in range(0, i2+1):
                for ii3 in range(0, i3+1):
                    for ii4 in range(0, i4+1):
                        for ii5 in range(0, i5+1):
                            for ii6 in range(0, i6+1):
                                G[ii1][ii2][ii3][ii4][ii5][ii6] += 1
    else:
        print("버그뜸!!!!!!!!!!!")
        return -1
    
    return G

if __name__ == "__main__":
    K1 = np.zeros(shape=(6))
    K2 = np.arange(6)
    K1 = np.array([2,2,0,0,0,0])
    K2 = np.array([0,0,0,0,0,0])
    K1_G = KtoK(K1)
    num = K1_G[K2[0]][K2[1]][K2[2]][K2[3]][K2[4]][K2[5]]
    print(num)
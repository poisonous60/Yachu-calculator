import numpy as np

#input
# H : numpy (6) array, [1짜리 킵 개수, 2짜리 킵 개수, ..., 6짜리 킵 개수], 현재 킵한 상태
# 킵 개수는 다 더해서 5여야 함
# output:
# G : int
# 그 족보에서 얻는 점수
def dice_num_correct_check(H):
    if H.sum() == 5:
        pass
    else:
        print("주사위가 5개가 아님")
        print("H: %s" %H)
def Aces(H):
    dice_num_correct_check(H)
    return H[0] * 1
def Deuces(H):
    dice_num_correct_check(H)
    return H[1] * 2
def Threes(H):
    dice_num_correct_check(H)
    return H[2] * 3
def Fours(H):
    dice_num_correct_check(H)
    return H[3] * 4
def Fives(H):
    dice_num_correct_check(H)
    return H[4] * 5
def Sixes(H):
    dice_num_correct_check(H)
    return H[5] * 6
def Choice(H):
    dice_num_correct_check(H)
    return (H[0]*1)+(H[1]*2)+(H[2]*3)+(H[3]*4)+(H[4]*5)+(H[5]*6)
def Four_of_a_Kind(H):
    dice_num_correct_check(H)
    swi = False
    for i in range(6):
        if H[i]>= 4:
            swi = True
    if swi:
        return (H[0]*1)+(H[1]*2)+(H[2]*3)+(H[3]*4)+(H[4]*5)+(H[5]*6)
    return 0
def Full_House(H):
    dice_num_correct_check(H)
    swi = False
    for i in range(6):
        for i2 in range(6):
            if H[i] == 2 and H[i2] == 3:
                swi = True
    if swi:
        return (H[0]*1)+(H[1]*2)+(H[2]*3)+(H[3]*4)+(H[4]*5)+(H[5]*6)
    return 0
def S_Straight(H):
    dice_num_correct_check(H)
    swi = False
    for i in range(3):
        if H[i] > 0 and H[i+1] > 0 and H[i+2] > 0 and H[i+3] > 0:
            swi = True
    if swi:
        return 15
    return 0
def L_Straight(H):
    dice_num_correct_check(H)
    swi = False
    for i in range(2):
        if H[i] > 0 and H[i+1] > 0 and H[i+2] > 0 and H[i+3] > 0 and H[i+4] > 0:
            swi = True
    if swi:
        return 30
    return 0
def Yacht(H):
    dice_num_correct_check(H)
    swi = False
    for i in range(6):
        if H[i] == 5:
            swi = True
    if swi:
        return 50
    return 0

if __name__ == "__main__":
    K1 = np.array([0, 0, 0,0,0,5])
    num = Aces(K1)
    print(num)
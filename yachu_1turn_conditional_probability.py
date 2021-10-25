import numpy as np
import yachuKtoK
import yachuJokbo as J
from anytree import Node, RenderTree
from enum import Enum
import sys
sys.setrecursionlimit(2000)

class Jocbo(Enum):
    Aces = 0
    Deduces = 1
    Threes = 2
    Fours = 3
    Fives = 4
    Sixes = 5
    Choice = 6
    Four_of_a_Kind = 7
    Full_House = 8
    S_Straight = 9
    L_Straight = 10
    Yacht = 11


# K1 = np.zeros(shape=(6))
# K2 = np.arange(6)
# K1 = np.array([2,2,0,0,0,0])
# K2 = np.array([0,0,0,0,0,0])
# K1_G = yachuKtoK.KtoK(K1)
# num = K1_G[K2[0]][K2[1]][K2[2]][K2[3]][K2[4]][K2[5]]
# print(num)

def print_score(arr1):
    print("Aces: %d" % J.Aces(arr1))
    print("Deuces: %d" % J.Deuces(arr1))
    print("Threes: %d" % J.Threes(arr1))
    print("Fours: %d" % J.Fours(arr1))
    print("Fives: %d" % J.Fives(arr1))
    print("Sixes: %d" % J.Sixes(arr1))
    print("Choice: %d" % J.Choice(arr1))
    print("Four_of_a_Kind: %d" % J.Four_of_a_Kind(arr1))
    print("Full_House: %d" % J.Full_House(arr1))
    print("S_Straight: %d" % J.S_Straight(arr1))
    print("L_Straight: %d" % J.L_Straight(arr1))
    print("Yacht: %d" % J.Yacht(arr1))
    return 0

def One_turn_2(arr1, arr2):
    conpro = yachuKtoK.KtoK(arr1)
    pro = conpro[arr2[0]][arr2[1]][arr2[2]][arr2[3]][arr2[4]][arr2[5]]
    return pro

def KtoK_to_pro(KtoKmap, arr2):
    return KtoKmap[arr2[0]][arr2[1]][arr2[2]][arr2[3]][arr2[4]][arr2[5]]

def CountToPro(i):
    return i/7776

# K1 = np.array([2,2,0,0,0,0])
# K2 = np.array([2,3,0,0,0,0])
# print(One_turn_2(K1, K2))
# print(CountToPro(One_turn_2(K1, K2)))
# print_score(K2)

## 가능하면 아래처럼 node set list를 하나 만들어서 관리해주는 것이 편함. 
all_node_set = []

## 새로운 변수를 추가해서 넣어줘도 상관없음. 
## 단 하나의 어떤 node에 data가 있을 경우 아래 모든 노드에서도 data를 넣어주어야 함
root = Node("Start", data=0,pro=1,arr=np.zeros(6),score=None)

all_node_set.append(root)

# for i in range(0, 3):
#     ## root.children은 기본적으로 tuple구조이며, 따라서 append등으로 새로운 값을 넣어줄 수 없음
#     ## 대신 아래처럼 새로운 node를 만들고, parent를 지정해주면 알아서 연결됨 
#     new_node = Node(f'child_{i}', parent=root, pro=0)
#     ## child가 추가되면 data를 변경하도록 세팅 
#     root.data+=1
#     all_node_set.append(new_node)
# Node("child_child_1", parent=root.children[0], pro=0)


keep_arr1 = np.array([0,0,0,0,0,0])
KtoKmap1 = yachuKtoK.KtoK(keep_arr1)
for i1 in range(0, 6):
    for i2 in range(0, 6):
        for i3 in range(0, 6):
            for i4 in range(0, 6):
                for i5 in range(0, 6):
                    for i6 in range(0, 6):
                        if (i1+i2+i3+i4+i5+i6) < 6:
                            keep_arr2 = np.array([i1, i2, i3, i4, i5, i6])
                            pro1 = KtoK_to_pro(KtoKmap1, keep_arr2)
                            pro1 = CountToPro(pro1)
                            new_node = Node(f'{i1}{i2}{i3}{i4}{i5}{i6}', parent=root, pro=pro1, data=0, arr=keep_arr2, score=None)
                            root.data+=1
                            all_node_set.append(new_node)

__print_i = 0
rows = root.children
for row in rows:
    KtoKmap2 = yachuKtoK.KtoK(row.arr)
    nodes_3_level = []
    sum_of_count = 0
    for i1 in range(0, 6):
        for i2 in range(0, 6):
            for i3 in range(0, 6):
                for i4 in range(0, 6):
                    for i5 in range(0, 6):
                        for i6 in range(0, 6):
                            if (i1+i2+i3+i4+i5+i6) == 5:
                                keep_arr3 = np.array([i1, i2, i3, i4, i5, i6])
                                pro2 = KtoK_to_pro(KtoKmap2, keep_arr3)
                                # pro2 = CountToPro(pro2)
                                if pro2 > 0:
                                    new_node = Node(f'{i1}{i2}{i3}{i4}{i5}{i6}', parent=row, pro=pro2, data=0, arr=keep_arr3, score=None)
                                    root.data+=1
                                    row.data+=1
                                    all_node_set.append(new_node)
                                    nodes_3_level.append(new_node)
                                    sum_of_count += pro2
                                    a = keep_arr3
                                    Jocbo_score = [J.Aces(a), J.Deuces(a), J.Threes(a), J.Fours(a), J.Fives(a), J.Sixes(a), \
                                        J.Choice(a), J.Four_of_a_Kind(a), J.Full_House(a), J.S_Straight(a), J.L_Straight(a), J.Yacht(a)]
                                    Node(f'{i1}{i2}{i3}{i4}{i5}{i6} Jokbo', parent=new_node, pro=None, data=None, arr=None, score=Jocbo_score)
    for node in nodes_3_level:
        node.pro = node.pro / sum_of_count

    print(__print_i)
    __print_i += 1

# f = open('2.txt', 'w')

print("=="*20)
## text상에서, tree를 예쁘게 볼 수 있음. 
for row in RenderTree(root):
    pre, fill, node = row
    print(f"{pre}{node.name}, data: {node.data}, pro: {node.pro}, arr: {node.arr}, score: {node.score}")
    # f.write(f"{pre}{node.name}, data: {node.data}, pro: {node.pro}, arr: {node.arr}, score: {node.score}")
    # f.write("\n")
print("=="*20)
## 기본적인 tree method를 지원
# print(f"children: { [c.name for c in root.children] }")
print(f"parent: {root.children[0].parent}")
print(f"is_root: {root.is_root}")
print(f"is_leaf: {root.is_leaf}")
## path ==> root부터 target_Node까지의 길을 말함. 
# target_node = root.children[0].children[0]
# print(f"path: {target_node.path}")
# print(f"ancestors: {target_node.ancestors}")
print("=="*20)

# f.close()

import random
from tqdm import tqdm


success = 0
fail = 0
tot_num = 2695483

for i in tqdm(range(tot_num)):
    random.seed(i**2 - i*4 + 17580) # 设定随机数种子
    car_index = random.randint(0,2) # 车的放置位置
    gates = [0, 0, 0] # 三扇门
    gates[car_index] = 1 # 把车放进门里

    first_select = random.randint(0,2) # 人第一次选择的门

    rm_gate = -1 # 初始化变量，打开的门
    if first_select == car_index: # 第一次选到车的情况
        rm_gate = random.randint(0,2) 
        if rm_gate == first_select: # 避免打开选到的门
            rm_gate = (rm_gate + 1) % 3

    if first_select != car_index: # 第一次没选到车
        rm_gate = 3 - first_select - car_index # 只能打开除去选到的和有车的门以外的最后一扇门

    last_gate = 3 - first_select - rm_gate # 未被打开且未被选择的门
    
    change_choice = random.randint(0,1) # 是否更改选项
    if change_choice == 0 and gates[first_select] == 1: #不更改选项，第一次选到车
        success += 1
    elif change_choice == 1 and gates[last_gate] == 1: # 更改选项，车在未被打开且未被选择的门里
        success += 1
    else : # 其他失败情况
        fail += 1

print("第二次成功次数：{}, 第二次失败次数：{}".format(success, fail))
print("第二次成功占比：{}，第二次失败占比：{}".format(success/tot_num, fail/tot_num))

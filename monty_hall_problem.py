import random

def raffleDoor(change = False):
    n = 1000000
    r = 0
    for _ in range(n):
        #随机生成三个门，其中一个为T另外两个为F
        number = random.randint(0,2)
        doors = [i==number for i in range(3)]

        #先随机打开一个门
        ext = doors.pop(random.randint(0,2))

        #排除一个假的门
        number = random.randint(0,1)
        if doors[number]:
            doors.pop(1^number)

        #是否要换
        if change:
            ext = doors[0]

        #记录结果
        if ext:
            r += 1

    return r/n

if __name__ == "__main__":
    print(raffleDoor())
    print(raffleDoor(True))
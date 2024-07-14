import random

def raffleDoor(change = False):
    n = 10000000
    r = 0
    for _ in range(n):
        #随机生成三个门，其中一个为T另外两个为F
        number = random.randint(0,2)
        doors = [i==number for i in range(3)]

        #先随机打开一个门
        ext = doors.pop(random.randint(0,2))

        """
        现在待选列表里有TF、FT、FF三种情况
        由于列表是随机的，不关注顺序，故将列表首项固定作为选择项
        于是TF可忽略
        FF与FT则将列表首项pop
        """

        #排除一个假的门
        if not doors[0]:
            doors.pop(0)

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
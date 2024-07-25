is_end = False
is_conflicted = False
time_count = 0
save_time = 0

class Marble:
    def __init__(self, x, y, weight, dir):
        self.x = x
        self.y = y
        self.weight = weight
        self.dir = dir

def is_conflict(marbleList):
    global is_conflicted, time_count, is_end, save_time
    new_marbleList = []
    out_count = 0
    flag = is_conflicted
    for i in range(len(marbleList)):
        if marbleList[i].x < -2 or marbleList[i].x > 2 or marbleList[i].y < -2 or marbleList[i].y > 2:
            out_count += 1
            continue
        for j in range(len(marbleList)):
            if i == j: continue
            
            if marbleList[i].x == marbleList[j].x and marbleList[i].y == marbleList[j].y:
                flag = True
                save_time = time_count
                if marbleList[i].weight > marbleList[j].weight or (marbleList[i].weight == marbleList[j].weight and i > j):
                    marbleList[j].weight = -1
                else:
                    marbleList[i].weight = -1
                    
    is_conflicted = flag
    if out_count == len(marbleList):
        is_end = True
    for marble in marbleList:
        if marble.weight != -1:
            new_marbleList.append(marble)
    return new_marbleList

def print_marble(marbleList):
    print()
    for marble in marbleList:
        print(marble.x, marble.y, marble.weight, marble.dir)
    print()
        
def move_marble(marbleList):
    global time_count, is_end, is_conflicted, save_time
    dir = [[0, 0.5], [-0.5, 0], [0, -0.5], [0.5, 0]]
    while not is_end:
        for marble in marbleList:
            marble.x += dir[marble.dir][0]
            marble.y += dir[marble.dir][1]
        time_count += 1
        marbleList = is_conflict(marbleList)
        
    if not is_conflicted: print(-1)
    else: print(save_time)
    return
    
def main():
    global is_end, time_count, is_conflicted
    testCase = int(input())
    marble_case = []
    for _ in range(testCase):
        marbleNum = int(input())
        marbleList = []
        for _ in range(marbleNum):
            marbleObj = list(input().split())
            if marbleObj[3] == 'U':
                d = 0
            elif marbleObj[3] == 'D':
                d = 2
            elif marbleObj[3] == 'L':
                d = 1
            elif marbleObj[3] == 'R':
                d = 3
            marbleList.append(Marble(int(marbleObj[0]), int(marbleObj[1]), int(marbleObj[2]), d))
        marble_case.append(marbleList)
        
    for t in range(testCase):
        is_end = False
        time_count = 0
        is_conflicted = False
        move_marble(marble_case[t])
        
    
if __name__ == "__main__":
    main()
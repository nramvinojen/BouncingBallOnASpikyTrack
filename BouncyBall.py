class ChoiceTree:
    
    def __init__(self, val = 0, speed = 0, sameSpd = None,  incSpd = None, decSpd = None):
        self.val = val
        self.speed = speed
        self.sameSpd = sameSpd
        self.incSpd = incSpd
        self.decSpd = decSpd

class BouncyBall:

    def __init__(self, iniSpeed, track):
        self.iniSpeed = iniSpeed
        self.track = track
    
    def buildTree(self):
        
        root = ChoiceTree(0, self.iniSpeed)
        stack = [root]
        count = 0
        while stack:

            if count == 10:
                break
            count += 1
            cur = stack.pop()

            curIdx = cur.val
            curSpeed = cur.speed

            if curIdx + curSpeed >= 0 and curIdx + curSpeed < len(self.track) and self.track[curIdx + curSpeed] != 1:
                cur.sameSpd = ChoiceTree(curIdx + curSpeed, curSpeed)
                stack.append(cur.sameSpd)
            if curIdx + curSpeed + 1 >= 0 and curIdx + curSpeed + 1 < len(self.track) and self.track[curIdx + curSpeed + 1 ] != 1:
                cur.incSpd = ChoiceTree(curIdx + curSpeed + 1, curSpeed + 1)
                stack.append(cur.incSpd)
            if curSpeed - 1 >= 0 and curIdx + curSpeed - 1 >= 0 and curIdx + curSpeed - 1 < len(self.track) and self.track[curIdx + curSpeed - 1 ] != 1:
                cur.decSpd = ChoiceTree(curIdx + curSpeed - 1, curSpeed - 1)
                stack.append(cur.decSpd)
        return root


    def traverseTree(self, root):

        stack = [root]

        while stack:
            cur = stack.pop()
            
            print(cur.val, cur.speed)

            if cur.speed == 0:
                return True

            
            if cur.sameSpd:
                stack.append(cur.sameSpd)
            if cur.incSpd:
                stack.append(cur.incSpd)
            if cur.decSpd:
                stack.append(cur.decSpd)

        return False





def main():
    print("----game 1----")
    track = [0,1,0,1,1,0,1,1,0,1]
    game1 = BouncyBall(3, track)
    print(list(range(len(track))))
    print(game1.track)
    gameTree = game1.buildTree()
    print(game1.traverseTree(gameTree))

    print("\n \n ----game 2----")
    track = [0,1,1,1]
    game1 = BouncyBall(2, track)
    print(list(range(len(track))))
    print(game1.track)
    gameTree = game1.buildTree()
    print(game1.traverseTree(gameTree))

    print("\n \n ----game 3----")
    track = [0,1,0,1,0,1,0,1,0, 0, 0, 1]
    game1 = BouncyBall(2, track)
    print(list(range(len(track))))
    print(game1.track)
    gameTree = game1.buildTree()
    print(game1.traverseTree(gameTree))

if __name__ == "__main__":
    main()
import random


class Player:
    def __init__(self, role="Player"):
        self.role = role


class Team:
    def __init__(self):
        self.team = [Player] * 9
        self.batter = 0

    def moveBatter(self):
        self.batter = (self.batter + 1) % 9


class Game:

    def __init__(self,teamA,teamB):
        self.Rui = [None] * 3
        self.point = [[0 for j in range(9)] for i in range(2)]
        self.team = 0
        self.kai = 0
        self.out = 0
        self.strike = 0
        self.ball = 0
        start = random.randint(0,1)
        if start == 0:
            self.first = teamA
            self.second = teamB
        else:
            self.first = teamB
            self.second = teamA
    def playball(self):
        print("Play Ball!!!!!!!")
        while self.kai < 9:
            print(str(self.kai+1) + "回", end="")
            if self.team == 0:
                print("表")
            else:
                print("裏")
            print("----------------------")
            while self.out < 3:
                self.fight()
            self.out = 0
            self.strike = 0
            self.ball = 0
            self.Rui = [None] * 3
            if self.team == 1:
                #回の更新
                self.team = 0
                self.kai += 1
            else:
                self.team = 1
    def NowPrint(self, blc, max):
        for i in range(blc):
            print("●", end="")
        for i in range(max-blc):
            print("○", end="")
        print("")


    def fight(self):
        print("S:", end="")
        self.NowPrint(self.strike,2)
        print("B:", end="")
        self.NowPrint(self.ball,3)
        print("O:", end="")
        self.NowPrint(self.out,2)
        print("ランナー:", end="")
        for i in range(3):
            if self.Rui[i] is not None:
                print(str(i+1) + "塁,",end="")
        print("")
        print("----------------------")
        cmd = input("コマンドを入力してください。")
        if cmd == "h":
            #init
            self.strike = 0
            self.ball = 0
            move = int(input("進塁した数を入力してください。"))
            if self.team == 0:
                self.hit(move,self.first.team[self.first.batter])
                self.first.moveBatter()
            else:
                self.hit(move,self.second.team[self.second.batter])
                self.second.moveBatter()
        elif cmd == "o":
            self.out += 1
            if self.team == 0:
                self.first.moveBatter()
            else:
                self.second.moveBatter()
        elif cmd == "s":
            self.strike += 1
            if self.strike > 2:
                self.out += 1
                self.strike = 0
                self.ball = 0
                if self.team == 0:
                    self.first.moveBatter()
                else:
                    self.second.moveBatter()
        elif cmd == "b":
            self.ball += 1
            if self.ball > 3:
                if self.team == 0:
                    self.hit(1, self.first.team[self.first.batter])
                    self.first.moveBatter()
                else:
                    self.hit(1, self.second.team[self.second.batter])
                    self.second.moveBatter()
                self.strike = 0
                self.ball = 0

    # move: ヒット数(デフォルト0)
    def hit(self, move=0, p=Player):
        Rui = [None] * 3
        Rui[move-1] = p
        for i in range(3):
            if self.Rui[i] is not None:
                # 人がいるため移動
                if i + move > 2:
                    # 点獲得
                    self.point[self.team][self.kai] += 1
                else:
                    Rui[i + move] = self.Rui[i]
        self.Rui = Rui


    def debug(self):
        print(self.point)
        print("---------------------")
        print(self.Rui)


if __name__ == "__main__":
    teamA = Team()
    teamB = Team()
    game = Game(teamA,teamB)
    game.playball()

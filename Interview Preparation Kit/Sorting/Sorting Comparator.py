from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return (self.name, self.score)

    # when sorting in ascending order, -1 is returned when a < b
    #                                  0 when a == b
    #                                  1 when a > b

    # note: we are still using this logic for sorting names since its alphabertical order

    # therefore, the opposite is the case for descending
    #                                  1 when a < b
    #                                  0 when a == b
    #                                  -1 when a > b
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name < b.name:
                return -.5
        # note that having the same name and score is a unecessary case
            else:
                return .5
        else:
            return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
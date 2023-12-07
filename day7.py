class Hand:
    strength={"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    def __init__(self, cards):
        self.cards=cards
        self.counts={}
        for card in cards:
            if card not in self.counts:
                self.counts[card]=0
            self.counts[card]+=1
        self.type=self.determine_type()
        
    def determine_type(self):
        if self.is5oak():
            return 6
        if self.is4oak():
            return 5
        if self.isfh():
            return 4
        if self.is3oak():
            return 3
        if self.is2p():
            return 2
        if self.is1p():
            return 1
        return 0
        

    def is5oak(self):
        return len(self.counts)==1

    def is4oak(self):
        if len(self.counts)==2:
            for n in self.counts.values():
                if n==1 or n==4:
                    return True
        return False
    
    def isfh(self):
        if len(self.counts)==2:
            for n in self.counts.values():
                if n==2 or n==3:
                    return True
        return False
    
    def is3oak(self):
        if len(self.counts)==3:
            for n in self.counts.values():
                if n==3:
                    return True
        return False
    
    def is2p(self):
        if len(self.counts)==3:
            for n in self.counts.values():
                if n==2:
                    return True
        return False
    
    def is1p(self):
        return len(self.counts)==4
    
    def ishc(self):
        return len(self.counts)==5
    
    def __eq__(self, other):
        return self.cards==other.cards
    
    def __lt__(self, other):
        if self.type<other.type:
            return True
        elif self.type>other.type:
            return False
        for card1, card2 in zip(self.cards, other.cards):
            if Hand.strength[card1]<Hand.strength[card2]:
                return True
            elif Hand.strength[card1]>Hand.strength[card2]:
                return False
    
    def __str__(self):
        return self.cards
    
class HandWithJoker(Hand):
    strength={"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    def __init__(self, cards):
        super().__init__(cards)
        self.type=self.determine_type()

    def determine_type(self):
        if "J" not in self.counts:
            return super().determine_type()
        options="AKQT98765432"
        maxtype=0
        for card in options:
            newhand=self.cards.replace("J", card)
            maxtype=max(maxtype, Hand(newhand).type)
        return maxtype
    
    def __lt__(self, other):
        if self.type<other.type:
            return True
        elif self.type>other.type:
            return False
        for card1, card2 in zip(self.cards, other.cards):
            if HandWithJoker.strength[card1]<HandWithJoker.strength[card2]:
                return True
            elif HandWithJoker.strength[card1]>HandWithJoker.strength[card2]:
                return False
    

        

def main():
    fname="day7_input.txt"
    hands=[]
    res=0
    with open(fname) as inputfile:
        for line in inputfile:
            hand, bid = line.strip().split()
            hands.append((HandWithJoker(hand), int(bid)))
    hands.sort()
    for i in range(len(hands)):
        res+=(i+1)*hands[i][1]
    print(res)
if __name__=="__main__":
    main()
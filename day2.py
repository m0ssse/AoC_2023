fname="day2_input.txt"
res=0
res2=0
total={"red": 12, "green": 13, "blue": 14}
with open(fname) as input_file:
    for row in input_file:
        parts=row.strip().split(": ")
        gameid=int(parts[0].split(" ")[1])
        sets=parts[1].split("; ")
        possible=True
        minimums={"red": 0, "green": 0, "blue": 0}
        for colors in sets:
            marbles=colors.split(", ")
            for marble in marbles:
                amount, color = marble.split()
                amount=int(amount)
                minimums[color]=max(minimums[color], amount)
                if amount>total[color]:
                    possible=False
        res2+=minimums["red"]*minimums["green"]*minimums["blue"]
        if possible:
            res+=gameid
print(res)
print(res2)
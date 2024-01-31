numheads = int(input("Сколько голов: "))
numlegs = int(input("Сколько ног: "))

def solve(fname, lname):
    step1 = fname * 2
    step2 = lname - step1
    rabbits = step2 / 2
    chickens = fname - rabbits
    print("в твоем загоне " + str(int(rabbits)) + " кроликов и " + str(int(chickens)) + " кур")

solve(numheads, numlegs)

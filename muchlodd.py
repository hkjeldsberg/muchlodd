import random
import time
import os
import sys



farger = ['\033[%im'%i for i in range(91, 97)]

def lotteri(mini,maxi,eks,eks2):

    brett = []
    min_spiller = mini
    max_spiller = maxi
    spillere = range(min_spiller, max_spiller+1)
    if eks != 0:
        spillere.remove(eks)
    if eks2 != 0:
        spillere.remove(eks2)
    spillere_verdi = [1]*(max_spiller+1)
    k = 60
    b = 3
    col = 1
    os.system("clear")
    print col*("-"*(b*k+8))
    for i, n in enumerate(spillere):
        brett.append((spillere_verdi[n]*str(n).rjust(2).ljust(b)).ljust(b*k) + "|" + "   " + " |")
        if spillere_verdi[n] > k:
            brett[i] = ((spillere_verdi[n]-1)*str(n).rjust(2).ljust(b)).ljust(b*k) + "| " + str(n) + " |"
        if (n+1) % 1000 == 0:
            print farger[i%6] + brett[i] + '\033[0m',
        else:
            print farger[i%6] + brett[i] + '\033[0m'
            print col*("-"*(b*k+8))
    print
    time.sleep(0.05)

    winner = 0
    while max(spillere_verdi) < k+1:
        tallet = random.choice(spillere)
        spillere_verdi[tallet] += 1
        brett = []
        os.system("clear")
        print col*("-"*(b*k+8))
        for i, n in enumerate(spillere):
            brett.append((spillere_verdi[n]*str(n).rjust(2).ljust(b)).ljust(b*k) + "|" + "   " + " |")
            if spillere_verdi[n] > k:
                brett[i] = ((spillere_verdi[n]-1)*str(n).rjust(2).ljust(b)).ljust(b*k) + "| " + str(n) + " |"
                winner = n, i
            if (n+1) % 1000 == 0:
                print farger[i%6] + brett[i] + '\033[0m',
            else:
                print farger[i%6] + brett[i] + '\033[0m'
                print col*("-"*(b*k+8))
            #print "-"*(b*k)
        print

        time.sleep(0.05)

    print
    #print farger[winner[1]%6] + "VINNEREN ER %d!!!!!!!!!!!!!!!!!!!!!" % winner[0] + '\033[0m'
    horizontal('    VINNEREN ER %d!!!!!' % winner[0], winner)

    # NOTE Masse tall!
    bigload = True
    if bigload:
        time.sleep(5.)
        os.system("clear")
        for i in range(1000):
            if i % 2 == 0:
                horizontal(8*("%d " %winner[0]),winner)
            else:
                horizontal(8*(" %d" %winner[0]),winner)
            time.sleep(0.25)



letterforms = '''\
       |       |       |       |       |       |       | |
  XXX  |  XXX  |  XXX  |   X   |       |  XXX  |  XXX  |!|
  X  X |  X  X |  X  X |       |       |       |       |"|
  X X  |  X X  |XXXXXXX|  X X  |XXXXXXX|  X X  |  X X  |#|
 XXXXX |X  X  X|X  X   | XXXXX |   X  X|X  X  X| XXXXX |$|
XXX   X|X X  X |XXX X  |   X   |  X XXX| X  X X|X   XXX|%|
  XX   | X  X  |  XX   | XXX   |X   X X|X    X | XXX  X|&|
  XXX  |  XXX  |   X   |  X    |       |       |       |'|
   XX  |  X    | X     | X     | X     |  X    |   XX  |(|
  XX   |    X  |     X |     X |     X |    X  |  XX   |)|
       | X   X |  X X  |XXXXXXX|  X X  | X   X |       |*|
       |   X   |   X   | XXXXX |   X   |   X   |       |+|
       |       |       |  XXX  |  XXX  |   X   |  X    |,|
       |       |       | XXXXX |       |       |       |-|
       |       |       |       |  XXX  |  XXX  |  XXX  |.|
      X|     X |    X  |   X   |  X    | X     |X      |/|
  XXX  | X   X |X     X|X     X|X     X| X   X |  XXX  |0|
   X   |  XX   | X X   |   X   |   X   |   X   | XXXXX |1|
 XXXXX |X     X|      X| XXXXX |X      |X      |XXXXXXX|2|
 XXXXX |X     X|      X| XXXXX |      X|X     X| XXXXX |3|
X      |X    X |X    X |X    X |XXXXXXX|     X |     X |4|
XXXXXXX|X      |X      |XXXXXX |      X|X     X| XXXXX |5|
 XXXXX |X     X|X      |XXXXXX |X     X|X     X| XXXXX |6|
XXXXXX |X    X |    X  |   X   |  X    |  X    |  X    |7|
 XXXXX |X     X|X     X| XXXXX |X     X|X     X| XXXXX |8|
 XXXXX |X     X|X     X| XXXXXX|      X|X     X| XXXXX |9|
   X   |  XXX  |   X   |       |   X   |  XXX  |   X   |:|
  XXX  |  XXX  |       |  XXX  |  XXX  |   X   |  X    |;|
    X  |   X   |  X    | X     |  X    |   X   |    X  |<|
       |       |XXXXXXX|       |XXXXXXX|       |       |=|
  X    |   X   |    X  |     X |    X  |   X   |  X    |>|
 XXXXX |X     X|      X|   XXX |   X   |       |   X   |?|
 XXXXX |X     X|X XXX X|X XXX X|X XXXX |X      | XXXXX |@|
   X   |  X X  | X   X |X     X|XXXXXXX|X     X|X     X|A|
XXXXXX |X     X|X     X|XXXXXX |X     X|X     X|XXXXXX |B|
 XXXXX |X     X|X      |X      |X      |X     X| XXXXX |C|
XXXXXX |X     X|X     X|X     X|X     X|X     X|XXXXXX |D|
XXXXXXX|X      |X      |XXXXX  |X      |X      |XXXXXXX|E|
XXXXXXX|X      |X      |XXXXX  |X      |X      |X      |F|
 XXXXX |X     X|X      |X  XXXX|X     X|X     X| XXXXX |G|
X     X|X     X|X     X|XXXXXXX|X     X|X     X|X     X|H|
  XXX  |   X   |   X   |   X   |   X   |   X   |  XXX  |I|
      X|      X|      X|      X|X     X|X     X| XXXXX |J|
X    X |X   X  |X  X   |XXX    |X  X   |X   X  |X    X |K|
X      |X      |X      |X      |X      |X      |XXXXXXX|L|
X     X|XX   XX|X X X X|X  X  X|X     X|X     X|X     X|M|
X     X|XX    X|X X   X|X  X  X|X   X X|X    XX|X     X|N|
XXXXXXX|X     X|X     X|X     X|X     X|X     X|XXXXXXX|O|
XXXXXX |X     X|X     X|XXXXXX |X      |X      |X      |P|
 XXXXX |X     X|X     X|X     X|X   X X|X    X | XXXX X|Q|
XXXXXX |X     X|X     X|XXXXXX |X   X  |X    X |X     X|R|
 XXXXX |X     X|X      | XXXXX |      X|X     X| XXXXX |S|
XXXXXXX|   X   |   X   |   X   |   X   |   X   |   X   |T|
X     X|X     X|X     X|X     X|X     X|X     X| XXXXX |U|
X     X|X     X|X     X|X     X| X   X |  X X  |   X   |V|
X     X|X  X  X|X  X  X|X  X  X|X  X  X|X  X  X| XX XX |W|
X     X| X   X |  X X  |   X   |  X X  | X   X |X     X|X|
X     X| X   X |  X X  |   X   |   X   |   X   |   X   |Y|
XXXXXXX|     X |    X  |   X   |  X    | X     |XXXXXXX|Z|
 XXXXX | X     | X     | X     | X     | X     | XXXXX |[|
X      | X     |  X    |   X   |    X  |     X |      X|\|
 XXXXX |     X |     X |     X |     X |     X | XXXXX |]|
   X   |  X X  | X   X |       |       |       |       |^|
       |       |       |       |       |       |XXXXXXX|_|
       |  XXX  |  XXX  |   X   |    X  |       |       |`|
       |   XX  |  X  X | X    X| XXXXXX| X    X| X    X|a|
       | XXXXX | X    X| XXXXX | X    X| X    X| XXXXX |b|
       |  XXXX | X    X| X     | X     | X    X|  XXXX |c|
       | XXXXX | X    X| X    X| X    X| X    X| XXXXX |d|
       | XXXXXX| X     | XXXXX | X     | X     | XXXXXX|e|
       | XXXXXX| X     | XXXXX | X     | X     | X     |f|
       |  XXXX | X    X| X     | X  XXX| X    X|  XXXX |g|
       | X    X| X    X| XXXXXX| X    X| X    X| X    X|h|
       |    X  |    X  |    X  |    X  |    X  |    X  |i|
       |      X|      X|      X|      X| X    X|  XXXX |j|
       | X    X| X   X | XXXX  | X  X  | X   X | X    X|k|
       | X     | X     | X     | X     | X     | XXXXXX|l|
       | X    X| XX  XX| X XX X| X    X| X    X| X    X|m|
       | X    X| XX   X| X X  X| X  X X| X   XX| X    X|n|
       |  XXXX | X    X| X    X| X    X| X    X|  XXXX |o|
       | XXXXX | X    X| X    X| XXXXX | X     | X     |p|
       |  XXXX | X    X| X    X| X  X X| X   X |  XXX X|q|
       | XXXXX | X    X| X    X| XXXXX | X   X | X    X|r|
       |  XXXX | X     |  XXXX |      X| X    X|  XXXX |s|
       |  XXXXX|    X  |    X  |    X  |    X  |    X  |t|
       | X    X| X    X| X    X| X    X| X    X|  XXXX |u|
       | X    X| X    X| X    X| X    X|  X  X |   XX  |v|
       | X    X| X    X| X    X| X XX X| XX  XX| X    X|w|
       | X    X|  X  X |   XX  |   XX  |  X  X | X    X|x|
       |  X   X|   X X |    X  |    X  |    X  |    X  |y|
       | XXXXXX|     X |    X  |   X   |  X    | XXXXXX|z|
  XXX  | X     | X     |XX     | X     | X     |  XXX  |{|
   X   |   X   |   X   |       |   X   |   X   |   X   |||
  XXX  |     X |     X |     XX|     X |     X |  XXX  |}|
 XX    |X  X  X|    XX |       |       |       |       |~|
'''.splitlines()

table = {}
for form in letterforms:
    if '|' in form:
        table[form[-2]] = form[:-3].split('|')
ROWS = len(table.values()[0])

def horizontal(word,winner):
    for row in range(ROWS):
        for c in word:
            print farger[winner[1]%6] + table[c][row] + '\033[0m',
        print
    print

def vertical(word):
    for c in word:
        for row in zip(*table[c]):
            print ' '.join(reversed(row))
        print



mini = int(input("Minimum: "))
maxi = int(input("Maximum: "))
eks = int(input("Eks: "))
eks2 = int(input("Eks2: "))
if maxi < mini:
    print("Trenger flere spillere!")
    import sys
    sys.exit(1)

lotteri(mini,maxi,eks,eks2)

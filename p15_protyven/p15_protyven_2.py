numbs = [i for i in range(2,11)]
cards = ["A"]+numbs+["J","Q","K"]
suits = ["diamonds", "clubs", "hearts", "spades"]
suits = str([(i+" ")*14 for i in suits]).split(" ")
suits = list(filter(str.isalpha, list(suits)))
card = zip(cards*13,suits)
iterab = iter(card)
try:
    n = int(input("Enter amount of printed cards (integer value): "))
except ValueError:
    print("Oh..Unlucky, but it's uncorrect.")
    raise SystemExit
for i in range(n):
    try:
        print(*next(iterab))
    except StopIteration:
        print("Stopping the iteration...That's all your cards!")
        break

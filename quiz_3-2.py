# Azaan Dawson amdg 1-12-21

def names_with(l):
  names_then_bets = ()
  iteration = 1
  names = []
  bet = []
  for i, v in enumerate(l):
    names.append(v[0])
    bet.append(v[1])
    bet.append(v[2])
    bet.append(v[3])
  names_then_bets = (names, bet)  
  return names_then_bets

ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]

print(names_with(ledger))

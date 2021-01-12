# Azaan Dawson amdg 1-12-21

def name_n_race_lst(y,r):
  final_lst = []
  for i, v in enumerate(y):
    lst = [(v, r[i])]
    final_lst += lst
  return final_lst

younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']
print(name_n_race_lst(younglings, race)

# Azaan Dawson
import random 
def clone_naming(x):
  your_clones = []
  while True:
    make_clones = input("Would You like to make a clone? (type 1 for yes and 2 for no) ")
    if int(make_clones) == 1:
      clone_num = random.randint(0 , 9999)
      if len(str(clone_num)) != 4:
        if 4 - len(str(clone_num)) == 3:
          print("Your new clone trooper is: {0}".format(x +'000'+ str(clone_num)))
          your_clones.append(x +'000'+ str(clone_num))
        elif 4 - len(str(clone_num)) == 2:
          print("Your new clone trooper is: {0}".format(x +'00'+ str(clone_num)))
          your_clones.append(x +'00'+ str(clone_num))
        else:
          print("Your new clone trooper is: {0}".format(x +'0'+ str(clone_num)))
          your_clones.append(x +'0'+ str(clone_num))  

      else:
        print("Your new clone trooper is: {0}".format(x +str(clone_num)))
        your_clones.append(x+str(clone_num))
    else:
      break     
  return your_clones

clone_given = "CT-"
print(clone_naming(clone_given))

# dictionary is a key value pair
# d1={}

# print(type(d1))

d2 = {"Parth": "Chupke se drop lutne vala",
      "Harsh": "Sabse pehle supply box lootne vala",
      "Hepin": "Playzone me knock hone vala noob",
      "Vatsal": "Game spectate krke dekhne vala"}

print("Enter Your Name\n")

ip = input()
word=ip.capitalize()
print(word,":", d2[word])

class player:
  def play(self):
     ptint:("The player is playing cricket ")
class Batsman(player):
  def play(self):
    print("The batsman is playing batting")
class Blower(player):
  def play(self):
    print("The bolwer is playing bowling")
batsman=Batsman()
blower=Blower()
batsman.play()
blower.play()


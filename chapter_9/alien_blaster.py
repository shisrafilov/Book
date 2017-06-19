# Demonstrates object interaction

class Player(object):
    """ A player in a shooter game """
    def blast(self, enemy):
        print("The player blasts an enemy")
        enemy.die()

class Alien(object):
    """ An alien in a shooter game """
    def die(self):
        print("Alien is dead")

# main
print("\t\tDeath of Alien")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter to exit")
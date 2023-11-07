class Ninja:
    def __init__(self, blood, chakra):
        self.blood = blood
        self.chakra = chakra

    def katon(self):
        print('Katon! Goukakyuu no Jutsu!')
        self.chakra -= 20

    def __str__(self):
        return 'blood ' + str(self.blood) + '\n' + 'chakra ' + str(self.chakra)


class Naruto(Ninja):

    def shadow_clone(self):
        print('Kage Bunshin no Jutsu!')
        self.chakra -= 100

    def rasengan(self):
        print('Rasengan!')
        self.chakra -= 500


n = Naruto(100, 2000)
n.shadow_clone()
n.rasengan()
print('blood '+str(n.blood))
print('chakra'+str(n.chakra))
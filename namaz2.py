class Namaz:  

    def __init__(self):
        self.farz=0

    def fazr(self):
        sunnah=2
        self.farz=2
        total = sunnah + self.farz
        print("total namaz in fazr : " + str(total))
        time=5
        if self.farz<time:
            print("Namaz is valid")
        else:
            return "Qaza"

    def zohar(self):
        sunnah=4+2
        self.farz=4
        total = sunnah + self.farz
        print("total namaz in zohar : " + str(total))

    def asr(self):
        sunnah=4
        self.farz=4
        total = sunnah + self.farz
        print("total namaz in asr : " + str(total))

    def magreeb(self):
        self.farz=3
        sunnah=2
        total = sunnah + self.farz
        print("total namaz in magreeb : " + str(total))

    def aesha(self):
        sunnah=4+2
        self.farz=4
        nafl=2
        witr=3
        total = sunnah + self.farz + nafl + witr
        print("total namaz in aesha : " + str(total))

    def Tfarz(self):
        farz= self.farz
        print(farz)

        if self.farz==4:
            print("Masha Allah")

        else:
            print("Total namaz not offered in a day ")

    


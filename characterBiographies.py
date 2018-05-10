class Wrestler:
    """This is the beginning of a class for the humble house wrestler"""

    def __init__(self, name):
        self.name = name

    def add_ringName(self, ringName):
        self.ringName = ringName

    def add_nicknames(self, nicknames):
        self.nicknames = nicknames

    def add_zodiac(self, zodiac):
        self.zodiac = zodiac
        
    def add_birthDate(self, birthDate):
        self.birthDate = birthDate

    def add_age(self, age):
        self.age = age

    def add_birthplace(self, birthplace):
        self.birthplace = birthplace

    def add_residence(self, residence):
        self.residence = residence

    def add_billedFrom(self, billedFrom):
        self.billedFrom = billedFrom

    def add_mass(self, mass):
        self.mass = mass

    def add_height(self, height):
        self.height = height

    def add_debut(self, debut):
        self.debut = debut

    def add_trainedBy(self, trainedBy):
        self.trainedBy = trainedBy
        
    def add_finishingMoves(self, finishingMoves):
        self.finishingMoves = finishingMoves

    def add_signatureMoves(self, signatureMoves):
        self.signatureMoves = signatureMoves

    #def add_entranceThemes(self, entranceThemes):
        #self.entranceThemes = entranceThemes

    def add_championships(self, championships):
        self.championships = championships

    def add_accomplishments(self, accomplishments):
        self.accomplishments = accomplishments

    def add_otherInfo(self, otherInfo):
        self.otherInfo = otherInfo

class Face(Wrestler):
    """Face inherits from Wrestler"""

class Tweener(Wrestler):
    """Tweener inherits from Wrestler"""

class Heel(Wrestler):
    """Heel inherits from Wrestler"""


a = Face("Aisha Sanaa Al-Amin")

a.add_ringName("Sanaa The Brilliant")

a.add_nicknames("The Miraculous One")

a.add_zodiac("Ram")

a.add_birthDate("April 7, 1994")

a.add_age(24)

a.add_birthplace("Latakia, Syria")

a.add_residence("Chicago, Illinois")

a.add_billedFrom("Latakia, Syria")

a.add_mass(201)

a.add_height(5)

a.add_debut("April 30, 2002")

a.add_trainedBy("Brave Hero")

a.add_finishingMoves("Praying Mantis")

a.add_signatureMoves("Spinning Crane Leg Kick")

# a.add_entranceThemes("")

a.add_championships("Heavyweight Championship")

a.add_accomplishments("Was voted the best female wrestler of the year in 2017")

a.add_otherInfo("Is a Hijabi Muslim")

print("\n\n")


o = Face("Ohiyesa Bidziil Adakai")

o.add_ringName("Bidziil Strong")

o.add_nicknames("The Galaxys Greatest")

o.add_zodiac("Taurus")

o.add_birthDate("May 3, 1983")

o.add_age(35)

o.add_birthplace("South Dakota, Minnesota")

o.add_residence("South Dakota, Minnesota")

o.add_billedFrom("South Dakota, Minnesota")

o.add_mass(190)

o.add_height(5)

o.add_debut("November 19, 1998")

o.add_trainedBy("The Bionic Man")

o.add_finishingMoves("Supernova Body Bomb")

o.add_signatureMoves("Lunar Assault")

# o.add_entranceThemes("")

o.add_championships("Intercontinental Championship")

o.add_accomplishments("Was voted the best face of the year in 2017")

o.add_otherInfo("Has a degree in Astrology")

print("\n\n")


c = Tweener("Chanda Ishita Anand")

c.add_ringName("Ishita Supreme")

c.add_nicknames("The Submission Specialist")

c.add_zodiac("Sagittarius")

c.add_birthDate("November 22, 2000")

c.add_age(18)

c.add_birthplace("Surat, India")

c.add_residence("Surat, India")

c.add_billedFrom("Surat, India")

c.add_mass(205)

c.add_height(6)

c.add_debut("December 22, 2014")

c.add_trainedBy("Sanaa The Brilliant")

c.add_finishingMoves("Octopus Grip")

c.add_signatureMoves("Sleeper Headlock")

# c.add_entranceThemes("")

c.add_championships("Universal Championship")

c.add_accomplishments("Was voted the best new wrestler of the year in 2017")

c.add_otherInfo("Knows seven languages")

print("\n\n")


p = Tweener("Anh Hào Phan")

p.add_ringName("Brave Hero")

p.add_nicknames("The Flying Specialist")

p.add_zodiac("Virgo")

p.add_birthDate("September 12, 1992")

p.add_age(26)

p.add_birthplace("Ha Long City, Vietnam")

p.add_residence("Da Nang, Vietnam")

p.add_billedFrom("Ho Chi Minh City, Vietnam")

p.add_mass(182)

p.add_height(5)

p.add_debut("December 12, 2012")
            
p.add_trainedBy("Adela Aeneas")

p.add_finishingMoves("Flying Chokeslam")

p.add_signatureMoves("Elevated Elbow Smash")

# p.add_entranceThemes("")

p.add_championships("Lightweight Championship")

p.add_accomplishments("Was voted the best male wrestler of the year in 2017")

p.add_otherInfo("Is deaf, but uses braille and sign language to communicate")

print("\n\n")


e = Heel("Adelita Eneida Holguín")

e.add_ringName("Adela Aeneas")

e.add_nicknames("Furious Adela")

e.add_zodiac("Leo")

e.add_birthDate("August 5, 1991")

e.add_age(27)

e.add_birthplace("Mérida, Mexico")

e.add_residence("Mérida, Mexico")

e.add_billedFrom("Mexico City, Mexico")

e.add_mass(180)

e.add_height(5)

e.add_debut("November 22, 2011")
            
e.add_trainedBy("Bidziil Strong")

e.add_finishingMoves("Firework Neckbreaker")

e.add_signatureMoves("Two-Handed Gut Buster")

# e.add_entranceThemes("")

e.add_championships("Lethal Championship")

e.add_accomplishments("Was voted the best heel of the year in 2017")

e.add_otherInfo("Won a gold medal for wrestling in the 2008 Summer Olympics")

print("\n\n")


b = Heel("Adir Boaz Hayes")

b.add_ringName("The Bionic Man")

b.add_nicknames("Strong and Swift")

b.add_zodiac("Capricorn")

b.add_birthDate("January 6, 1978")

b.add_age(40)

b.add_birthplace("New York, New York")

b.add_residence("Miami, Florida")

b.add_billedFrom("Miami, Florida")

b.add_mass(290)

b.add_height(6)

b.add_debut("January 1, 1994")
            
b.add_trainedBy("Himself")

b.add_finishingMoves("Shooting Star Spinning Kick")

b.add_signatureMoves("Bionic Elbow Drop")

# b.add_entranceThemes("")

b.add_championships("Ultimate Championship")

b.add_accomplishments("Has the longest undefeated streak ever")

b.add_otherInfo("Has a prosthetic arm")

print(a.name)
print(a.ringName)
print(a.nicknames)
print(a.zodiac)
print(a.birthDate)
print(a.age)
print(a.birthplace)
print(a.residence)
print(a.billedFrom)
print(a.mass)
print(a.height)
print(a.debut)
print(a.trainedBy)
print(a.finishingMoves)
print(a.signatureMoves)
#print(a.entranceThemes)
print(a.championships)
print(a.accomplishments)
print(a.otherInfo)

print("\n\n")

print(o.name)
print(o.ringName)
print(o.nicknames)
print(o.zodiac)
print(o.birthDate)
print(o.age)
print(o.birthplace)
print(o.residence)
print(o.billedFrom)
print(o.mass)
print(o.height)
print(o.debut)
print(o.trainedBy)
print(o.finishingMoves)
print(o.signatureMoves)
#print(o.entranceThemes)
print(o.championships)
print(o.accomplishments)
print(o.otherInfo)

print("\n\n")

print(c.name)
print(c.ringName)
print(c.nicknames)
print(c.zodiac)
print(c.birthDate)
print(c.age)
print(c.birthplace)
print(c.residence)
print(c.billedFrom)
print(c.mass)
print(c.height)
print(c.debut)
print(c.trainedBy)
print(c.finishingMoves)
print(c.signatureMoves)
#print(c.entranceThemes)
print(c.championships)
print(c.accomplishments)
print(c.otherInfo)

print("\n\n")

print(p.name)
print(p.ringName)
print(p.nicknames)
print(p.zodiac)
print(p.birthDate)
print(p.age)
print(p.birthplace)
print(p.residence)
print(p.billedFrom)
print(p.mass)
print(p.height)
print(p.debut)
print(p.trainedBy)
print(p.finishingMoves)
print(p.signatureMoves)
#print(p.entranceThemes)
print(p.championships)
print(p.accomplishments)
print(p.otherInfo)


print("\n\n")

print(e.name)
print(e.ringName)
print(e.nicknames)
print(e.zodiac)
print(e.birthDate)
print(e.birthplace)
print(e.residence)
print(e.age)
print(e.billedFrom)
print(e.mass)
print(e.height)
print(e.debut)
print(e.trainedBy)
print(e.finishingMoves)
print(e.signatureMoves)
#print(e.entranceThemes)
print(e.championships)
print(e.accomplishments)
print(e.otherInfo)

print("\n\n")

print(b.name)
print(b.ringName)
print(b.nicknames)
print(b.zodiac)
print(b.birthDate)
print(b.age)
print(b.birthplace)
print(b.residence)
print(b.billedFrom)
print(b.mass)
print(b.height)
print(b.debut)
print(b.trainedBy)
print(b.finishingMoves)
print(b.signatureMoves)
#print(b.entranceThemes)
print(b.championships)
print(b.accomplishments)
print(b.otherInfo)





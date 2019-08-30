import random
import constvals as cv

class Language:

    def __init__(self):

        
        self.wordOrder = random.sample(["S","V","O"],3)

        self.morphology = random.choice(cv.MORPHOLOGY_TYPES)

        numLetters = random.randint(25,40)
        numVowels = int(numLetters * random.uniform(0.2,0.4))

        self.vowels     = random.sample(cv.VOWELS, numVowels)
        self.consonants = random.sample(cv.CONSONANTS, numLetters - numVowels)

        self.codaChance = random.choice([0,1,random.random()]) 
        self.onsetChance = random.choice([0,1,random.random()]) if self.codaChance != 0 else 1

        if self.onsetChance != 0:
            self.onsetCons = random.sample(self.consonants, random.randint(
                                                        int(len(self.consonants)/2),
                                                        len(self.consonants)
                                                        ))
        if self.codaChance != 0:
            self.codaCons = random.sample(self.consonants, random.randint(
                                                        int(len(self.consonants)/2),
                                                        len(self.consonants)
                                                        ))
        self.maxNucleusLen = random.randint(1,3)
        self.minMorphemeLen    = random.randint(1,2)
        self.maxMorphemeLen    = random.randint(2,3)

        self.languageName = self.newMorpheme().capitalize()
        
    def newMorpheme(self):
        m = ""

        for _ in range(random.randint(self.minMorphemeLen,self.maxMorphemeLen)):
            if(random.random()<self.onsetChance):
                m += random.choice(self.onsetCons)
            
            for n in range(random.randint(1, self.maxNucleusLen)):
                m += random.choice(self.vowels) 
                
            if(random.random()<self.codaChance):
                m += random.choice(self.codaCons)

        return m
        
    def printInfo(self):
        print("This is a language called " + self.languageName )
        print("Word order is " + str(self.wordOrder)  )
        print("Morphology is " + str(self.morphology) )
        print("Vowels are " + str(self.vowels) )
        print("Consonants are " + str(self.consonants) )
        print(self.maxNucleusLen)
        print(self.minMorphemeLen)
        print(self.maxMorphemeLen)
        print("Example morphemes:")
        print(self.newMorpheme())
        print(self.newMorpheme())
        print(self.newMorpheme())

if __name__ == "__main__":
    exLang = Language()
    exLang.printInfo()
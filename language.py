import random
from . import constvals as cv

from . import phonology
from . import vocabulary


class Language:
    def __init__(self):

        self.wordOrder = random.sample(["S", "V", "O"], 3)

        self.morphology = random.choice(cv.MORPHOLOGY_TYPES)

        numLetters = random.randint(7, 26)
        numVowels = min(int(numLetters * random.uniform(0.3, 0.5)), 6)

        self.phonology = phonology.newPhonology()

        self.sylRules = phonology.newSyllableRules(self.phonology)

        self.maxNucleusLen = random.randint(1, 3)
        self.minMorphemeLen = random.randint(1, 2)
        self.maxMorphemeLen = random.randint(2, 3)

        self.marksNumber = random.choice([True, False])

        self.dictionary = vocabulary.newVocabulary(self.newMorpheme)
        self.languageName = self.newMorpheme().capitalize()

    def newMorpheme(self):
        m = ""

        for _ in range(random.randint(self.minMorphemeLen,
                                      self.maxMorphemeLen)):
            if (random.random() < self.sylRules['onset']['chance']):
                m += random.choice(self.sylRules['onset']['cons'])

            for n in range(random.randint(1, self.maxNucleusLen)):
                m += random.choice(self.phonology['vows'])

            if (random.random() < self.sylRules['coda']['chance']):
                m += random.choice(self.sylRules['coda']['cons'])

        return m

    def printInfo(self):
        print("This is a language called " + self.languageName)
        print("Word order is " + str(self.wordOrder))
        print("Morphology is " + str(self.morphology))
        print(self.phonology)
        print(self.sylRules)
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

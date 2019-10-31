import random
import constvals as cv


def newPhonology():
    numLetters = random.randint(7, 26)
    numVowels = min(int(numLetters * random.uniform(0.3, 0.5)), 6)
    vowels = random.sample(cv.VOWELS, numVowels)
    consonants = random.sample(cv.CONSONANTS, numLetters - numVowels)

    return {"vows": vowels, "cons": consonants}


def newSyllableRules(phono):
    sylRules = {}
    for c in ['coda', 'onset']:
        sylRules[c] = {}
        sylRules[c]['chance'] = random.choice([0, 1, random.random()])

        sylRules[c]['cons'] = random.sample(
            phono['cons'],
            random.randint(int(len(phono['cons']) / 2), len(phono['cons'])))
    if sylRules['coda']['chance'] == 0:
        sylRules['onset']['chance'] = 1

    return sylRules

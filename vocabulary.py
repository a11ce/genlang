from pathlib import Path


def newVocabulary(newMorphemeF):
    vocab = {}
    with open(Path(__file__).parent / 'words.ls') as f:
        curCat = ""
        for line in f:
            if line[0] == ";":
                #print(line[1:].strip())
                curCat = line[1:].strip()
                vocab[curCat] = {}
            else:
                vocab[curCat][line.strip()] = newMorphemeF()
    #print(vocab)
    return vocab

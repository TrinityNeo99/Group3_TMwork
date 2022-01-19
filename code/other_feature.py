import spacy
nlp = spacy.load('en_core_web_sm')
from read_corpus import read_in_conll_file, list_of_tokens

def tokenlist2doc(token_list):
    str = ' '
    doc = str.join(token_list)
    return doc


def get_lemma(nlp_doc):
    for token in nlp_doc:
        print(token.text, " lemma->", token.lemma_)

def get_PoS(nlp_doc):
     for token in nlp_doc:
        print(token.text, " PoS tag->", token.tag_)


def is_neg_suff(token):
    ret = 0
    Neg_suffix=['less', 'free']
    for suf in Neg_suffix:
        start = token.find(suf)
        end = start + len(suf)
        if end == len(token) and start != -1:
            print("Negation suffix: ",token, suf)
            ret = 1
    return ret


def is_neg_inff(token):
    ret = 0
    Neg_inffix=['less', 'free']
    for inf in Neg_inffix:
        start = token.find(inf)
        end = start + len(inf)
        if end < len(token) and start != -1:
            print("Negation inffix: ", token, inf)
            ret = 1
    return ret



if __name__ == "__main__":
    test = ["apples", "boy", "cat", "men", "homeless", "homelesses"]
    for t in test:
        is_neg_suff(t)
        is_neg_inff(t)


    path = "bioscope.clinical.columns(1).txt"
    path = "SEM-2012-SharedTask-CD-SCO-dev-simple.v2.txt"
    path = "SEM-2012-SharedTask-CD-SCO-training-simple.v2.txt"
    conll = read_in_conll_file(path)
    tokenlist = list_of_tokens(conll)
    for t in tokenlist:
        is_neg_suff(t)
        is_neg_inff(t)
    # doc = tokenlist2doc(tokenlist)
    # nlp_doc = nlp(doc)
    # get_lemma(nlp_doc)
    # get_PoS(nlp_doc)
    print("finish")
import csv
import sys

def read_in_conll_file(conll_file, delimiter='\t'):
    '''
    Read in conll file and return structured object

    :param conll_file: path to conll_file
    :param delimiter: specifies how columns are separated. Tabs are standard in conll

    :returns structured representation of information included in conll file
    '''
    my_conll = open(conll_file, 'r', encoding='utf-8')
    conll_as_csvreader = csv.reader(my_conll, delimiter=delimiter, quoting=csv.QUOTE_NONE)
    return conll_as_csvreader

def get_token(row):
    # print(row)
    return row[3]

def get_negcue_label(row):
    return row[4]

def list_of_tokens(csv_object):
    tokens = []
    for row in csv_object:
        if len(row) == 0:
            continue
        tokens.append(get_token(row))
    return tokens

def main(args=None):
    if not args:
        args = sys.argv
    path = args[1]
    conll = read_in_conll_file(path)
    tokenlist = list_of_tokens(conll)
    print(tokenlist)

# args = ['x', r'C:\Users\Tessel Wisman\Documents\TextMining\AppliedTMMethods\bioscope-corpus\bioscope.clinical.columns.txt']
# args = ['x', r"bioscope.clinical.columns(1).txt"]
# main(args)

"""
Routine to load master dicitonary
Version for LM 2020 Master Dictionary

Bill McDonald
Date: 201510 Updated: 202201
"""

import datetime as dt


def load_masterdictionary(file_path, print_flag=False, f_log=None, get_other=False):
    start_local = dt.datetime.now()
    # Setup dictionaries
    _master_dictionary = {}
    _sentiment_categories = ['negative', 'positive', 'uncertainty', 'litigious', 
                             'strong_modal', 'weak_modal', 'constraining']
    _sentiment_dictionaries = dict()
    for sentiment in _sentiment_categories:
        _sentiment_dictionaries[sentiment] = dict()
   
    # Load slightly modified common stopwords. 
    # Dropped from traditional: A, I, S, T, DON, WILL, AGAINST
    # Added: AMONG
    _stopwords = ['ME', 'MY', 'MYSELF', 'WE', 'OUR', 'OURS', 'OURSELVES', 'YOU', 'YOUR', 'YOURS',
                  'YOURSELF', 'YOURSELVES', 'HE', 'HIM', 'HIS', 'HIMSELF', 'SHE', 'HER', 'HERS', 'HERSELF',
                  'IT', 'ITS', 'ITSELF', 'THEY', 'THEM', 'THEIR', 'THEIRS', 'THEMSELVES', 'WHAT', 'WHICH',
                  'WHO', 'WHOM', 'THIS', 'THAT', 'THESE', 'THOSE', 'AM', 'IS', 'ARE', 'WAS', 'WERE', 'BE',
                  'BEEN', 'BEING', 'HAVE', 'HAS', 'HAD', 'HAVING', 'DO', 'DOES', 'DID', 'DOING', 'AN',
                  'THE', 'AND', 'BUT', 'IF', 'OR', 'BECAUSE', 'AS', 'UNTIL', 'WHILE', 'OF', 'AT', 'BY',
                  'FOR', 'WITH', 'ABOUT', 'BETWEEN', 'INTO', 'THROUGH', 'DURING', 'BEFORE',
                  'AFTER', 'ABOVE', 'BELOW', 'TO', 'FROM', 'UP', 'DOWN', 'IN', 'OUT', 'ON', 'OFF', 'OVER',
                  'UNDER', 'AGAIN', 'FURTHER', 'THEN', 'ONCE', 'HERE', 'THERE', 'WHEN', 'WHERE', 'WHY',
                  'HOW', 'ALL', 'ANY', 'BOTH', 'EACH', 'FEW', 'MORE', 'MOST', 'OTHER', 'SOME', 'SUCH',
                  'NO', 'NOR', 'NOT', 'ONLY', 'OWN', 'SAME', 'SO', 'THAN', 'TOO', 'VERY', 'CAN',
                  'JUST', 'SHOULD', 'NOW', 'AMONG']

    # Loop thru words and load dictionaries
    with open(file_path) as f:
        _total_documents = 0
        _md_header = f.readline()  # Consume header line
        print()
        for line in f:
            cols = line.rstrip('\n').split(',')
            word = cols[0]
            _master_dictionary[word] = MasterDictionary(cols, _stopwords)
            for sentiment in _sentiment_categories:
                if getattr(_master_dictionary[word], sentiment):
                    _sentiment_dictionaries[sentiment][word] = 0
            _total_documents += _master_dictionary[cols[0]].doc_count
            if len(_master_dictionary) % 5000 == 0 and print_flag:
                print(f'\r ...Loading Master Dictionary {len(_master_dictionary):,}', end='', flush=True)

    if print_flag:
        print('\r', end='')  # clear line
        print(f'\nMaster Dictionary loaded from file:\n  {file_path}\n')
        print(f'  master_dictionary has {len(_master_dictionary):,} words.\n')

    if f_log:
        try:
            f_log.write('\n\n  FUNCTION: load_masterdictionary' +
                        '(file_path, print_flag, f_log, get_other)\n')
            f_log.write(f'\n    file_path  = {file_path}')
            f_log.write(f'\n    print_flag = {print_flag}')
            f_log.write(f'\n    f_log      = {f_log.name}')
            f_log.write(f'\n    get_other  = {get_other}')
            f_log.write(f'\n\n    {len(_master_dictionary):,} words loaded in master_dictionary.\n')
            f_log.write(f'\n    Sentiment:')
            for sentiment in _sentiment_categories:
                f_log.write(f'\n      {sentiment:13}: {len(_sentiment_dictionaries[sentiment]):8,}')
            f_log.write(f'\n\n  END FUNCTION: load_masterdictionary: {(dt.datetime.now()-start_local)}')
        except Exception as e:
            print('Log file in load_masterdictionary is not available for writing')
            print(f'Error = {e}')

    if get_other:
        return _master_dictionary, _md_header, _sentiment_categories, _sentiment_dictionaries, _stopwords, _total_documents
    else:
        return _master_dictionary


class MasterDictionary:
    def __init__(self, cols, _stopwords):
        for ptr, col in enumerate(cols):
            if col == '':
                cols[ptr] = '0'
        try:
            self.word = cols[0].upper()
            self.sequence_number = int(cols[1])    
            self.word_count = int(cols[2])
            self.word_proportion = float(cols[3])
            self.average_proportion = float(cols[4])
            self.std_dev_prop = float(cols[5])
            self.doc_count = int(cols[6])
            self.negative = int(cols[7])
            self.positive = int(cols[8])
            self.uncertainty = int(cols[9])
            self.litigious = int(cols[10])
            self.strong_modal = int(cols[11])
            self.weak_modal = int(cols[12])
            self.constraining = int(cols[13])
            self.syllables = int(cols[14])
            self.source = cols[15]
            if self.word in _stopwords:
                self.stopword = True
            else:
                self.stopword = False
        except:
            print('ERROR in class MasterDictionary')
            print(f'word = {cols[0]} : seqnum = {cols[1]}')
            quit()
        return

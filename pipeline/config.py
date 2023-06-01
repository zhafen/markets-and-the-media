'''This config file contains global parameters for the analysis,
i.e. parameters for which the values are needed for multiple files.
Parameters that are critical but are only used in one file are also here.
'''

from datetime import datetime

# Parameters dictionary
pm = {
    # Identifying information for the company in question.
    'organizations': [ 'Google Inc', 'Alphabet Inc' ],
    'keyword': 'google',
    
    # Time ranges
    'start_date': datetime(2020,1,1),
    'end_date': datetime(2022,12,31),
    # Everything between start_date_test and end_date is part of the test data set.
    # Everything between start_date and start_date_test is part of the training data set.
    'start_date_test': datetime(2022,1,1),
}
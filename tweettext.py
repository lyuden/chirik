
from chirplib.followgraph import name_number_correspondence, numbered_filename, number_from_filename
import os


def parse_ut_folder(path):

    '''
    Extracts data from one userTweets folder.

    @path - path to said folder

    '''

def number_tweets(ut_path):
    
    '''
    This function provides iterator of tuples of  all tweets from userTweets folder prepended with userid

    i.e. (number, 'tweet text')

    '''

    for name in os.listdir(ut_path):
    
        num_filename = numbered_filename(os.path.join(ut_path,name))

        
        if not (num_filename is None):

            full_path = os.path.join(ut_path,os.path.join(name,num_filename))

            id_num = number_from_filename(num_filename)
            
            with open(full_path) as tweetfile:

                for line in tweetfile:
                    yield (id_num,line)

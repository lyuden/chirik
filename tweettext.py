
from chirik.followgraph import name_number_correspondence, numbered_filename, number_from_filename
import os
import re

from chirik.individual import mentions_wrapper

pattern = re.compile('[^\w ]+')

def parse_ut_folder(path):

    '''
    Extracts data from one userTweets folder.

    @path - path to said folder

    '''

    pass

def cached(func):

    def wrapper(cache):


        if cache is None:

            return func

        else:

            def wrapper_second(path):

                result = func(path)

                for r in result:
                    if not( r in cache):

                        cache.add(r)
                        yield r

            return wrapper_second

    return wrapper
                

#@mentions_wrapper
@cached
def number_tweets(ut_path):
    
    '''
    This function provides iterator of tuples of  all tweets from userTweets folder prepended with userid

    i.e. (number, 'tweet text')

    

    '''




    
    

    #print "UT PATH", ut_path
    
    num_filename = numbered_filename(ut_path)

        
    if not (num_filename is None):

        full_path = os.path.join(ut_path,num_filename)

        id_num = number_from_filename(num_filename)
            
        with open(full_path) as tweetfile:

            for line in tweetfile:
                yield (id_num, pattern.sub('',line))

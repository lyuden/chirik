
from chirik.followgraph import name_number_correspondence, numbered_filename, number_from_filename
import os
import re
from itertools import ifilter



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
#@cached
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





def prepare_dir_iterator(path,dirname):

    '''
    Returns iterator of all dirs in tree under @path
    whose parent dir has name @dirname

    '''

    for dirpath in ifilter(lambda x: dirname in os.path.basename(os.path.dirname(x[0])),os.walk(path)):

        yield dirpath


def is_tweetfile(walk_el):

    return len(walk_el[2])==1 and len(re.findall('[0-9]+[.]txt',walk_el[2][0]))==1

    
def name_from_ut_path(ut_path):


    return os.path.basename(ut_path)

    
        
def user_tweets_filepaths(path):



    for tweetfile in ifilter(is_tweetfile , prepare_dir_iterator(path,'userTweets')):


        yield {'name':name_from_ut_path(tweetfile[0]),
                'id':int(os.path.splitext(tweetfile[2][0])[0]),
                'fullpath':os.path.join(tweetfile[0],tweetfile[2][0])
        }



def name_number_tweets(path):


    for tweetfile in user_tweets_filepaths(path):

        with open(tweetfile['fullpath']) as fileread:

            for line in fileread.readlines():

                yield {'name':tweetfile['name'],
                       'id':tweetfile['id'],
                       'text':pattern.sub('',line),
                       'fullpath':tweetfile['fullpath']
                }



def name_id_set(path):


    return set((tf['name'],tf['id']) for tf in user_tweets_filepaths(path))
        
        

                
def unique_number_tweets(path):

    number_tweets=set([])

    for tweet in name_number_tweets(path):

        marker = (tweet['id'],hash(tweet['text']))

        if not (marker in number_tweets):

            number_tweets.add(marker)

            yield tweet

            

import os
from itertools import ifilter


def prepare_dir_iterator(path,dirname):

    '''
    Returns iterator of all dirs in tree under @path
    whose parent dir has name @dirname

    '''

    for dirpath in ifilter(lambda x: dirname in os.path.basename(os.path.dirname(x[0])),os.walk(path)):

        yield dirpath[0]


    

"""

def parse_one_crawl_dir(path, namefunc,tweetfunc):

    '''
    Parse one crawl dir, this dir is usually have name like

    crawl_2013_1_10_3

    and inside have following structure

    ..\
       followers
       following
       searchtweets
       urlcontents
       userTweets



    namecache is a cache of name number correspondences
    '''



    user_following=following_tuples(os.path.join(path,'following'))
    user_followers=following_tuples(os.path.join(path,'followers'))

    name_numbers = namefunc(os.path.join(path,'userTweets'))
    tweets = tweetfunc(os.path.join(path,'userTweets'))
    

    return (user_following,user_followers,name_numbers,tweets)



'''

    namecache ={}

    tweetset = set([])

    mentions = defaultdict(list)

    if individ_path is None:

        tweetfunc = number_tweets(tweetset)

        namefunc = partial(namecache,name_number_correspondence)

    else:

        wordlist = collect_words(individ_path)

        tweetfunc = mentions_wrapper(mentions,wordlist)(tweetset)

        #    name_number_correspondence(,namecache)


'''

    
'''
def parse_all_crawls(path,tweetprocessor,nameprocessor):

    """
'''
    Parses all subdirectories of @path wich contain "crawl" in name


    returns array of iteratosr
    '''
    
"""

    
    crawl_dirs=[dirpath for dirpath in os.listdir(path) if 'crawl' in dirpath]

    results=[parse_one_crawl_dir(os.path.join(path,crawl_dir),nameprocessor,tweetprocessor) for crawl_dir in crawl_dirs]

    t_results = zip(*results)

    #print t_results
    
    return ([chain.from_iterable(result) for result in t_results])
  '''     






    





    
    
        
        
    
    
                        





def main(results,namecache,path):

    followers_iter = followers_wrapper(mix_followers(results[0],results[1]))

    tweet = results[2]

    namenumber = results[3]


    
    write_results(tweet,namenumber,followers_iter, namecache,path)

"""
    

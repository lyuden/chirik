import os
from chirik.followgraph import following_tuples,name_number_correspondence, mix_followers

from chirik.tweettext import number_tweets

from itertools import chain

from functools import partial

FOLLOWER_LINK_TEMPLATE= "{} {}\n"
NUMBER_TWIT_TEMPLATE= "{} {}\n"
NAME_NUMBER_TEMPLATE= "{} {}\n"


def parse_one_crawl_dir(path):

    user_following=following_tuples(os.path.join(path,'following'))
    user_followers=following_tuples(os.path.join(path,'followers'))

    name_numbers = name_number_correspondence(os.path.join(path,'userTweets'))
    tweets = number_tweets(os.path.join(path,'userTweets'))
    

    return (user_following,user_followers,name_numbers,tweets)



    
    
def parse_all_crawls(path):

    crawl_dirs=[dirpath for dirpath in os.listdir(path) if 'crawl' in dirpath]


    results=[parse_one_crawl_dir(os.path.join(path,crawl_dir)) for crawl_dir in crawl_dirs]

    t_results = zip(*results)

    #print t_results
    
    return [chain.from_iterable(result) for result in t_results]
    

    
def write_results(results, path):

    pathdir=partial(os.path.join,path)

    follow_path = pathdir('follow_graph.txt')
    tweet_path = pathdir('number_tweets.txt')
    name_number_path = pathdir('name_number.txt')

    with open(follow_path,'w') as ffile:

        for ff_pair in mix_followers(results[0],results[1]):

            ffile.write(FOLLOWER_LINK_TEMPLATE.format(*ff_pair))


    with open(tweet_path,'w') as tfile:


        for tw in results[3]:

            tfile.write(NUMBER_TWIT_TEMPLATE.format(*tw))

    with open(name_number_path,'w') as nnfile:


        for nn in results[2]:

            nnfile.write(NAME_NUMBER_TEMPLATE.format(*nn))

       

    
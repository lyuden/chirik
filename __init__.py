from chirik.individual import mentions_wrapper,collect_words, followers_wrapper
from chirik.followgraph import mix_followers 
from chirik.flow import dataflow_generator

from chirik.serialize import  write_iterator, write_followers, write_individ_tweets
from chirik.followgraph import following_tuples,name_number_correspondence, mix_followers
from chirik.tweettext import number_tweets


from functools import partial
from constants import NUMBER_TWIT_TEMPLATE, NAME_NUMBER_TEMPLATE
from collections import defaultdict


import os


    
def main(args):

    dataflow_gen = dataflow_generator(args.path)

    # Creating function for processing tweet lines that will not allow dublicates
    tweetcache= set([])
    tfunc = number_tweets(tweetcache)
    tweet_flow = dataflow_gen('userTweets',tfunc)
    mentions= defaultdict(list)


    
    # Creating function for getting names that will store information in namecache
    namecache = {}
    nfunc = partial(name_number_correspondence,namecache)
    name_flow= dataflow_gen('userTweets',nfunc)


    wordlist = collect_words(args.ifolder)
    mention_wrapped_tweet_iterator= mentions_wrapper(mentions,wordlist,tweet_flow)

    
    user_following=dataflow_gen('following',following_tuples)
    user_followers=dataflow_gen('followers',following_tuples)



    # Calculating output files names
    pathdir=partial(os.path.join,args.output)
    follow_path = pathdir('follow_graph.txt')
    tweet_path = pathdir('number_tweets.txt')
    name_number_path = pathdir('name_number.txt')

    
    # Consuming all tweetflow iterator and populating mentions
    write_iterator(tweet_path,NUMBER_TWIT_TEMPLATE, mention_wrapped_tweet_iterator)

    # Consuming all nameflow iterator and populating namecache
    write_iterator(name_number_path,NAME_NUMBER_TEMPLATE, name_flow)


    # Uniting data frol followers and following subfolders
    mix = mix_followers(user_following,user_followers)

    inv_namecache = {v:k for k, v in namecache.items()}
    
    #Creating wrapper that will process individual followers data
    
    wrapped_followers = followers_wrapper(args.ifolder,mentions,namecache, inv_namecache)(mix)

    
    #Consuming wrapped_followers iterator 
    
    write_followers(wrapped_followers, inv_namecache, follow_path)


    #Writing individual tweets

    write_individ_tweets(args.ifolder,mentions)

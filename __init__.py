from chirik.individual import collect_words, find_mentions, write_individual_followers
from chirik.followgraph import mix_followers 
from chirik.flow import dataflow_generator

from chirik.serialize import  write_iterator, write_followers, write_individ_tweets
from chirik.followgraph import following_tuples,name_number_correspondence, mix_followers
from chirik.tweettext import number_tweets, unique_number_tweets,name_id_set, name_number_tweets


from functools import partial
from constants import NUMBER_TWIT_TEMPLATE, NAME_NUMBER_TEMPLATE
from collections import defaultdict
from itertools import chain

import os


def create_number_tweets_file(output,root):


    num_tweet_gen = ((tw['id'],tw['text']) for tw in unique_number_tweets(root))
    write_iterator(output,NUMBER_TWIT_TEMPLATE,num_tweet_gen)

def create_number_names_file(output,root):
    write_iterator(output,NAME_NUMBER_TEMPLATE, name_id_set(root))


def create_followers_file(output,root,inv_namecache):

    dataflow_gen = dataflow_generator(root)
    user_following=dataflow_gen('following',following_tuples)

    user_followers=dataflow_gen('followers',following_tuples)

    # Uniting data frol followers and following subfolders
    mix = set(chain(user_following,user_followers))


    #Consuming wrapped_followers iterator 
    
    write_followers(mix, inv_namecache, output)




    

def generate_mentions(root,ifolder):

    mentions= defaultdict(list)

    wordlist = collect_words(ifolder)
    #mention_wrapped_tweet_iterator= mentions_wrapper(mentions,wordlist,unique_tweet_set)
    names = [f['first'] for f in wordlist]


    #print names,wordlist

    for tweetline in unique_number_tweets(root):


        #including all tweets by user listed as first word
        # if this tweet is by some user listed as first word in individual files
        if tweetline['name'] in names:
                    
            mentions[tweetline['name']].append(tweetline)


        # if somebody mentions some user listed as first word in individual files

        tweettext = tweetline['text']
        user_mentions=[ew['first'] for ew in wordlist if tweettext.find(ew['first'])>=0]
        
        second_word_mentions = [ew['first'] for ew in wordlist if tweettext.find(ew['second'])>=0]

        residue_mentions = [ew['first'] for ew in wordlist if
                            
                            reduce (lambda a,v: a or v,
                                    [tweettext.find(s)>=0 for s in ew['residue']], False)]
        
        for mention in user_mentions+second_word_mentions+residue_mentions:

            mentions[mention[0]].append(tweetline)

    #print "\n Mentions\n",mentions
    return mentions


def create_individual_followers_files(individ_path,root,iout, mentions,nameset,inv_namecache):



    dataflow_gen = dataflow_generator(root)    
    
    user_following=dataflow_gen('following',following_tuples)
    user_followers=dataflow_gen('followers',following_tuples)

    # Uniting data frol followers and following subfolders
    
    mix = set(chain(user_following,user_followers))
    
    #Creating wrapper that will process individual followers data

    #print mix,mentions
    
    write_individual_followers(individ_path,iout,mentions,nameset, inv_namecache,mix)

    #assert False

    #def create_file_mentions(root,ifolder):

    

    
    
def main(args):

    

    # Creating function for processing tweet lines that will not allow dublicates
    tweetcache= set([])

    # Calculating output files names
    pathdir=partial(os.path.join,args.output)
    follow_path = pathdir('follow_graph.txt')
    tweet_path = pathdir('number_tweets.txt')
    name_number_path = pathdir('name_number.txt')


    #unique_tweet_set = set(dataflow_gen('userTweets',number_tweets))

    if args.ioutfolder =='':
        ioutfolder = args.ifolder
    else:

        ioutfolder = args.ioutfolder
    
    create_number_tweets_file(tweet_path,args.path)


    create_number_names_file(name_number_path,args.path)
                

    
    # Creating set with all known names and ids
    nameset = name_id_set(args.path)

    #print nameset, args.path

    namedict = dict(nameset)

    inv_namecache = {v:k for k, v in namedict.items()}

    create_followers_file(follow_path,args.path,inv_namecache)

    if os.path.exists(ioutfolder):

        mentions= generate_mentions(args.path,args.ifolder)

        create_individual_followers_files(args.ifolder,args.path,ioutfolder,
                                      mentions,namedict,inv_namecache)
    

        #Writing individual tweets

        write_individ_tweets(args.ifolder,ioutfolder,mentions)

    

import os

from chirik.individual import collect_words, extract_words

from constants import FOLLOWER_LINK_TEMPLATE,NAME_NUMBER_TEMPLATE,NUMBER_TWIT_TEMPLATE



from chirik.followgraph import number_to_number_and_name

def write_individ_tweets(individ_path,ioutfolder,mentions):


    wordlist = collect_words(individ_path)

    #print mentions.keys()

    for filename in os.listdir(individ_path):


        result = extract_words(os.path.join(individ_path,filename))

        speaker,word = result['first'],result['second']

        with open(os.path.join(ioutfolder,filename.split('.txt')[0] + "_tweets.txt"),'w') as tweetfile:
            for line in mentions[speaker]:
                tweetfile.write(NUMBER_TWIT_TEMPLATE.format(line['id'],line['text']))
                            


'''
def write_individ_followers(individ_path,path_to_followers,mentions):


    
    wordlist = collect_words(individ_path)


    for filename in os.listdir(individ_path):


        speaker,word = extract_word(os.path.join(individ_path,filename))

        with open(os.path.join(individ_path,filename + "_followers",'w')
              ) as tweetfile:
            for line in mentions[speaker]:
                    tweetfile.write(NUMBER_TWIT_TEMPLATE.format(*line))

'''                    
    
    
def write_followers(followers_iter,inv_namecache,follow_path):



    with open(follow_path,'w') as ffile:

        for followed,follower in followers_iter:

            #print followed,follower

            res = number_to_number_and_name(followed,inv_namecache)+ number_to_number_and_name(follower,inv_namecache)

            ffile.write(FOLLOWER_LINK_TEMPLATE.format(*res ))



def write_iterator(filepath,template, iterator):

    with open(filepath,'w') as sfile:

        for iteritem in iterator:
            sfile.write(template.format(*iteritem))
    
"""
def write_results(tweet,namenumber,follow,namecache, path):
    

    '''
    This function writes out three files in path


    follow_graph.txt - file containing



    

    '''

    pathdir=partial(os.path.join,path)

    follow_path = pathdir('follow_graph.txt')
    tweet_path = pathdir('number_tweets.txt')
    name_number_path = pathdir('name_number.txt')


    


    write_iterator(tweet_path,NUMBER_TWIT_TEMPLATE, tweet)

    write_iterator(name_number_path,NAME_NUMBER_TEMPLATE, namenumber)

    write_followers(follow,namecache,follow_path)
"""            

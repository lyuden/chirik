import os
from collections import defaultdict

from constants import FOLLOWER_LINK_TEMPLATE
from chirik.followgraph import number_to_number_and_name


def extract_words(path_to_file):

    '''
    Extracting tuple containing user handle and first following word separated by ,

    '''

    
    with open(path_to_file) as individual_file:

        contents =(individual_file.read()).split(',')

        result_list = contents[0].split(" ")

        result = { 'first':result_list[0],
                   'second':" ".join(result_list[1:]),
                   'residue':tuple(contents[1:])} 

    return result
    

def get_name_generator(namecache):

    def get_number(name):

        def evaluator():

            return namecache['name']

        return evaluator

    return get_number
    
    
def collect_words(path):


    '''
    Creating wordlist for using in find_mentions from given path

    '''
    
    return [extract_words(os.path.join(path,flnm)) for flnm in os.listdir(path)]



def write_individual_followers(individ_path,individ_output,mentions,namecache,inv_namecache,followiter):


    


    # Creating array of files we would write to ignoring all _tweets and _follow_graph ones
    files_to_write = [(
    extract_words(
        os.path.join(individ_path,filename)),
    open(os.path.join(individ_output,filename.split('.txt')[0] +"_follow_graph.txt"),'w'))
        for filename in os.listdir(individ_path) if (not('follow_graph' in filename)) and (not ('_tweets' in filename))]

    filehandle_dict = dict([(namecache[filehandle[0]['first']], filehandle)  for filehandle in files_to_write ])

    # Creating cache of all id's of users that's assosiated with every individual user
    mention_idn_cache = {}

    for name in filehandle_dict:

        idn = inv_namecache[name]
        
        mention_idn_cache[idn]=tuple(mention['id'] for mention in  mentions[idn])


    # Taking all followers one by one and checking if they are satisfy conditions
        
    for item in followiter:


        # If this followed follower pairs followed is amongst indiwiduals we write down
        if item[0] in filehandle_dict:

            towrite = number_to_number_and_name(item[0],inv_namecache)+number_to_number_and_name(item[1],inv_namecache)
            filehandle_dict[item[0]][1].write(FOLLOWER_LINK_TEMPLATE.format(*towrite))

        else:


            # If this followed in mentions for some user we write him down in according file
            for name in filehandle_dict:

                idn = inv_namecache[name]

                if item[0] in mention_idn_cache[idn]:

                    towrite = number_to_number_and_name(item[0],inv_namecache)+number_to_number_and_name(item[1],inv_namecache)
                    #print towrite
                    filehandle_dict[name][1].write(FOLLOWER_LINK_TEMPLATE.format(*towrite))


    for filehandle in files_to_write:

        filehandle[1].close()



    
    
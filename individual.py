import os
from collections import defaultdict

from constants import FOLLOWER_LINK_TEMPLATE
from chirik.followgraph import number_to_number_and_name


def find_mentions(wordlist,tweetline):

    '''
    Returns list of user handlers whos 'words' are in this tweetline

    '''


    #print wordlist,tweetline
    return [(ew['first'],tweetline) for ew in wordlist if tweetline.find(ew['second'])>=0]



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



def followers_wrapper(individ_path,mentions,namecache,inv_namecache):


    

    def wrapper(iterfunc):

        print 'Namecache', namecache

        files_to_write = [(
        extract_words(
            os.path.join(individ_path,filename)),
        open(filename.split('.txt')[0] +"_follow_graph.txt",'w'))
        for filename in os.listdir(individ_path)]

        filehandle_dict = dict([(namecache[filehandle[0]['first']], filehandle)  for filehandle in files_to_write ])

        
        for item in iterfunc:

            print item[0],item,filehandle_dict
            if item[0] in filehandle_dict:

                towrite = number_to_number_and_name(item[0],inv_namecache)+number_to_number_and_name(item[1],inv_namecache)
                filehandle_dict[item[0]][1].write(FOLLOWER_LINK_TEMPLATE.format(*towrite))

            yield item

        for filehandle in files_to_write:

            filehandle[1].close()

    return wrapper

    
def mentions_wrapper(mention_accum,wordlist,tweetiter):

    '''
    

    '''

    for tweetline in tweetiter:

                #including all tweets by user listed as first word
                if tweetline[0] in wordlist:
                    
                    mention_accum[tweetline[0]].append(tweetline)

                for mention in find_mentions(wordlist,tweetline[1]):

                    mention_accum[mention[0]].append(tweetline)

                yield tweetline





    
        
        


            
    
    
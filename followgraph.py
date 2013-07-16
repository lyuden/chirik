

import os
import pprint

from itertools import chain

def numbered_filename(pathname):

    infolder = os.listdir(pathname)

    if len(infolder)>0:
        return infolder[0]
    else:
        return None

def number_to_number_and_name(number,namecache):


    return (number, ((namecache[number]) if (number in namecache) else 'NAMENOTFOUND'))
    
        
def number_from_filename(filename):
    
    return int(os.path.splitext(filename)[0])

    
def name_number_correspondence(cache,path, unique = True):


    #print cache

    #print os.listdir(path),path

    name = os.path.basename(path)
    
    for num_filename in os.listdir(path):
    
        #num_filename = numbered_filename(os.path.join(path,name))


        if not (num_filename is None):

            candidate= (name,
                   number_from_filename(num_filename))


            if candidate[0] in cache:

                assert candidate[1]==cache[candidate[0]]

            else:

                cache[candidate[0]]=candidate[1]

                yield candidate
            


def following_tuples(path):

    name = os.path.basename(path)




    num_filename = numbered_filename(path)

    if not (num_filename is None):
        
        u_number = number_from_filename(num_filename)
        
        with open(os.path.join(path,num_filename)) as filename:
            for latter in filename:
                yield (u_number,int(latter.strip()))

def reverse_tuples(tupleiter):

    for tup in tupleiter:

        yield (tup[1],tup[0])

                    
def mix_followers(user_following,user_followers, cache = None):

            
    #follow_set = set(user_following)



    followers_reversed =reverse_tuples(user_followers)

    #follow_set.update(followers_reversed)

    if cache is None:
        for item in chain(user_following,followers_reversed):
            yield item

    else:
        for item in chain(user_following,followers_reversed):

            if not(item in cache):
                cache.add(item)
                yield item





    
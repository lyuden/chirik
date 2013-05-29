import os
import pprint

from itertools import chain

def numbered_filename(pathname):

    infolder = os.listdir(pathname)

    if len(infolder)>0:
        return infolder[0]
    else:
        return None

    
        
def number_from_filename(filename):
    
    return int(os.path.splitext(filename)[0])

    
def name_number_correspondence(path):

    for name in os.listdir(path):
    
        num_filename = numbered_filename(os.path.join(path,name))

        if not (numbered_filename is None):

            yield (name,
                   number_from_filename(num_filename))



def following_tuples(path):

    names = os.listdir(path)

    for name in names :

        pathname = os.path.join(path,name)
        num_filename = numbered_filename(pathname)

        if not (num_filename is None):

            u_number = number_from_filename(num_filename)
        
            with open(os.path.join(pathname,num_filename)) as filename:
                for latter in filename:
                    yield (u_number,int(latter.strip()))

def reverse_tuples(tupleiter):

    for tup in tupleiter:

        yield (tup[1],tup[0])

                    
def mix_followers(user_following,user_followers):

            
    #follow_set = set(user_following)

    followers_reversed =reverse_tuples(user_followers)

    #follow_set.update(followers_reversed)


    return chain(user_following,followers_reversed)
    
    





    
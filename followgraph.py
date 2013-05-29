import os
import pprint

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

    names=os.listdir(path)

    for name in names :

        pathname=os.path.join(path,name)

        num_filename = numbered_filename(pathname)

        if not (num_filename is None):
            
            with open(os.path.join(pathname,num_filename)) as filename:
                for latter in filename:
                    yield (number_from_filename(num_filename),int(latter.strip()))


def mix_followers(user_following,user_followers):

    

        #for i3,e3 in enumerate(e):
            
        #    print e3

        #    if i3 >10:
        #        break
    
            
    follow_set=set(user_following)


    g=((t[1],t[0]) for t in user_followers)

    

    follow_set.update(g)

    return follow_set
    
    





    
from chirik.individual import find_mentions

from chirik.followgraph import mix_followers

#from chirik.flow import main_flow

from chirik import main

from nose.tools import nottest


from  collections import defaultdict

from chirik.constants import NAME_NUMBER_TEMPLATE, NUMBER_TWIT_TEMPLATE

from chirik.serialize import write_iterator, write_followers, write_individ_tweets

import tempfile
import shutil
import re
import os

from os.path import join as pjoin

UT1_CONTENTS = '''@user2 Reply to u2 tweet
dog cat cow #animals
Romney Obama #politicians
'''

UT2_CONTENTS = '''@user1 Reply to u1 tweet
falcon eagle sparrow #birds
Hussein Hitler #evil
'''

UT3_CONTETS = """USER3TWEET
"""

d={'111':UT1_CONTENTS,
'222':UT2_CONTENTS,
'333':UT3_CONTETS}
patt = re.compile('[^\w ]+')
TWEETS_ANSWER= '\n'.join([a+' '+patt.sub('',s)  for a in d for s in d[a].split('\n') if s !='' ])

@nottest
def test_find_mentions():

    res = find_mentions({"a":'b'}, "b")
    assert res == [('a','b')]


def mock_tweetline_iter(ut_path):

    for c in enumerate("buble dump".split()):

        yield c

        
@nottest
def test_mentions_wrapper():


    m = defaultdict(list)


    wordlist = {'42':'b', '8':'d'}


    #mit = mentions_wrapper(m,wordlist,mock_tweetline_iter(''))

    #for item in mit:

    #    print item
    
    #print m

    assert m['8'] == ['dump']

    assert m['42'] == ['buble']


def prepare_mock_crawl():


    tmpdir = tempfile.mkdtemp()

    utwtdir=os.path.join(tmpdir,'userTweets')

    followersdir=os.path.join(tmpdir,'followers')
    followingdir=os.path.join(tmpdir,'following')

    os.mkdir(utwtdir)

    os.mkdir(followersdir)

    os.mkdir(followingdir)

    utu1dir=os.path.join(utwtdir,'user1')
    utu2dir=os.path.join(utwtdir,'user2')
    utu3dir=os.path.join(utwtdir,'user3')

    os.mkdir(utu1dir)
    os.mkdir(utu2dir)
    os.mkdir(utu3dir)


    with open(os.path.join(utu1dir,'111.txt'),'w') as utwrite:

        utwrite.write(UT1_CONTENTS)

    with open(os.path.join(utu2dir,'222.txt'),'w') as utwrite:

        utwrite.write(UT2_CONTENTS)
        
    with open(os.path.join(utu3dir,'333.txt'),'w') as utwrite:

        utwrite.write(UT3_CONTETS)


    fldr1 = os.path.join(followersdir,'user1')
    fldr2 = os.path.join(followersdir,'user2')


    
    os.mkdir(fldr1)
    os.mkdir(fldr2)

    with open(pjoin(fldr1,'111.txt'),'w') as flnfile:

        flnfile.write('222\n333\n')

    with open(pjoin(fldr2,'222.txt'),'w') as flnfile:

        flnfile.write('111\n333\n')


    
    flngdir1 =os.path.join(followingdir,'user1')
    flngdir2 =os.path.join(followingdir,'user2')
    flngdir3 =os.path.join(followingdir,'user3')

    os.mkdir(flngdir1)
    os.mkdir(flngdir2)
    os.mkdir(flngdir3)

    with open(pjoin(flngdir1,'111.txt'),'w') as flnfile:

        flnfile.write('222\n')

    with open(pjoin(flngdir1,'222.txt'),'w') as flnfile:
        
        flnfile.write('111\n')
        
        
    with open(pjoin(flngdir3,'333.txt'),'w') as flnfile:
        
        flnfile.write('111\n222\n')
    

    return tmpdir
    
    
def prepare_mock_individ_dir():

    
    tmpdir = tempfile.mkdtemp()

    idir =pjoin(tmpdir,'individ')
    os.mkdir(idir)


    with open(pjoin(
                    pjoin(tmpdir,'individ'),
                    'i1.txt')
                    , 'w') as indfile:

        indfile.write("user1 sparrow")
    

    return idir
    
class FakeArgs:
    def __init__(self,path,out,ind):

        self.path = path
        self.output = out
        self.ifolder = ind

@nottest    
def test_construct_functions():

    mock_ind = prepare_mock_individ_dir()

    mock_crawl = prepare_mock_crawl()

    mock_out = tempfile.mkdtemp()


    tmpdir = tempfile.mkdtemp()

    main(FakeArgs(mock_crawl,mock_out,mock_ind))


    with open(pjoin(mock_out,'name_number.txt')) as nn:

        test_names = nn.read()

    assert test_names == "user1 111\nuser2 222\nuser3 333\n"


    with open(pjoin(mock_out,'number_tweets.txt')) as nn:

        test_names = nn.read()

    
    assert test_names == TWEETS_ANSWER+'\n'


    assert os.path.exists(pjoin(mock_ind,'i1_tweets.txt'))

    with open(pjoin(mock_ind,'i1_tweets.txt')) as indtweets:

        indtweetscont =indtweets.read()


    print mock_out,mock_ind
    #print indtweetscont

    with open(pjoin(mock_ind,'i1_follow_graph.txt')) as indtweets:

        print indtweets.read()


    assert indtweetscont == "222 falcon eagle sparrow birds\n"

    assert False
    

if __name__ == "__main__":

    test_construct_functions()
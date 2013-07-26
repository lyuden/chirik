from nose.tools import nottest
import tempfile
import os

from chirik.test_individual import prepare_mock_crawl, TWEETS_ANSWER, prepare_mock_individ_dir, write_individ_tweets

from chirik import create_number_names_file, create_number_tweets_file,create_followers_file, create_individual_followers_files, generate_mentions

from chirik.tweettext import name_id_set





def test_create_number_tweets_file():


    
    tmpdir = tempfile.mkdtemp()

    crawldir = prepare_mock_crawl()


    outfile_path =os.path.join(tmpdir,'test_number_tweets.txt')

    create_number_tweets_file(outfile_path,crawldir)

    with open(outfile_path) as fileread:

        result = fileread.read()

    
    assert result ==TWEETS_ANSWER+"\n"

    

def test_create_number_names_file():


    tmpdir = tempfile.mkdtemp()

    crawldir = prepare_mock_crawl()


    outfile_path =os.path.join(tmpdir,'test_number_names.txt')

    create_number_names_file(outfile_path,crawldir)

    with open(outfile_path) as fileread:

        result = fileread.read()

    print result, zip(result+"   ","user1 111\nuser2 222\nuser3 333\n")
    assert set(result.split('\n')) == set("user1 111\nuser2 222\nuser3 333\n".split("\n"))

    
    
def test_create_followers_file():

    tmpdir = tempfile.mkdtemp()
    crawldir = prepare_mock_crawl()
    outfile_path =os.path.join(tmpdir,'test_followers.txt')
    namedict = dict(name_id_set(crawldir))

    inv_namecache = {v:k for k, v in namedict.items()}

    create_followers_file(outfile_path,crawldir,inv_namecache)

    with open(outfile_path) as fileread:

        result = fileread.read()

    test=('111,user1 333,user3',
        '222,user2 111,user1',
        '111,user1 222,user2',
        '333,user3 111,user1',
        '333,user3 222,user2',
        '222,user2 333,user3')

    flag = True
    for sample in test:

        flag = flag and sample in result.split('\n')

        
        
    print result,inv_namecache
    assert flag

def test_create_individual_followers_files():

    tmpdir = tempfile.mkdtemp()
    crawldir = prepare_mock_crawl()
    ifolder = prepare_mock_individ_dir()
    namedict = dict(name_id_set(crawldir))

    inv_namecache = {v:k for k, v in namedict.items()}

    mentions = generate_mentions(crawldir,ifolder)

    

    nameset = name_id_set(crawldir)
        
    namedict = dict(nameset)

    inv_namecache = {v:k for k, v in namedict.items()}

    print mentions.keys()

    create_individual_followers_files(ifolder,crawldir,ifolder,
                                      mentions,namedict,inv_namecache)


    outfile_path =os.path.join(ifolder,'i1_follow_graph.txt')
    with open(outfile_path) as fileread:

        result = fileread.read()

    test=('111,user1 333,user3',
        '222,user2 111,user1',
        '111,user1 222,user2',
        '222,user2 333,user3')

    flag = True
    for sample in test:

        flag = flag and sample in result.split('\n')

    
    print ifolder
    assert flag

@nottest
def test_write_individ_tweets():

    crawldir = prepare_mock_crawl()
    ifolder = prepare_mock_individ_dir()

    mentions = generate_mentions(crawldir,ifolder)

    
    write_individ_tweets(ifolder,ifolder,mentions)

    print ifolder

    assert False
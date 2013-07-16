from chirik.tweettext import number_tweets

from chirik.test_individual import prepare_mock_crawl

import tempfile

from os.path import join

def test_number_tweets():

    mock_crawl = prepare_mock_crawl()


    cache = set([])

    ite = number_tweets(cache)(join(mock_crawl,'userTweets/user1'))

    res = [i for i in ite]

    assert res[0][0]==111

    assert res[0][1].find('user2')>-1
    
    

    
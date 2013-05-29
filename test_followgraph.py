import unittest
import os
from chirik.followgraph import parse_one_crawl_dir, following_tuples

BASEDIR="/media/DATA/Work/crawls/"
TEST_CRAWL='crawl_2013_1_10_3'

class TestFollowerGraph(unittest.TestCase):


    def test_following_tuples(self):

        pass


    def test_parse_one_crawl(self):

        g1,g2,g3 = parse_one_crawl_dir(os.path.join(BASEDIR,TEST_CRAWL))


        #print len([g for g in g1])

        mainset=set([(g[1],g[0]) for g in g1])

        mainset.update(g2)

        print len(mainset)
        


            
        


if __name__ == "__main__":

    unittest.main()
        
        
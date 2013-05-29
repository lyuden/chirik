from chirik.crawl import parse_one_crawl_dir, parse_all_crawls,write_results
import argparse
import os

CRAWL_DIR_TEMPLATE=['following','followers','userTweets','urlcontents', 'searchtweets']

parser = argparse.ArgumentParser(description="This is program for parsing twitter crawls")


parser.add_argument("--following-only", help="Use only follower followers information from 'following'' folder", action='store_true', default=False)
parser.add_argument("--followers-only", help="Use only follower followers information from 'followers'' folder",action='store_true', default=False)

parser.add_argument("path", type = str,  help ="Path to directory with data to parse")

parser.add_argument("--output-folder", dest = 'output',help="Path to folder where result files would be written. Default is current dir",default='.')



def run_interface(args=None):

    if args is None:

        args = parser.parse_args()


    dirlist = os.listdir(args.path)


    if reduce (lambda c,a : a  and (c in CRAWL_DIR_TEMPLATE),dirlist,True):

        results = parse_one_crawl_dir(args.path)
    else:
        results=parse_all_crawls(args.path)
        
            
    write_results(results,args.output)        

        


    


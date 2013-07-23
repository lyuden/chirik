
import argparse
import os

CRAWL_DIR_TEMPLATE=['following','followers','userTweets','urlcontents', 'searchtweets']

parser = argparse.ArgumentParser(description="This is program for parsing twitter crawls")


parser.add_argument("--following-only", help="Use only follower followers information from 'following'' folder", action='store_true', default=False)
parser.add_argument("--followers-only", help="Use only follower followers information from 'followers'' folder",action='store_true', default=False)

parser.add_argument("path", type = str,  help ="Path to directory with data to parse")

parser.add_argument("--output-folder", dest = 'output',help="Path to folder where result files would be written. Default is current dir",default='.')

parser.add_argument("--individuals-folder", dest = "ifolder", help = "Path to folder that contains files with user name see README 'Individual files'" ,default = "./individual")

parser.add_argument("--ind-output-folder", dest = "ioutfolder", help = "Path to folder where individual files reaults would be outputted by default it is output to individual folder 'Individual files'" ,default = "")


def run_interface(args=None):

    if args is None:

        args = parser.parse_args()


    return args




        


    


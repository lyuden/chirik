from itertools import imap,chain

from functools import partial

from chirik.crawl import prepare_dir_iterator

from chirik.followgraph import following_tuples,name_number_correspondence, mix_followers

def dataflow_generator(path):

    dir_iterator_gen = partial(prepare_dir_iterator,path)

    def dataflow(dirname,processor):


        return chain.from_iterable(imap(processor,dir_iterator_gen(dirname)))

    return dataflow



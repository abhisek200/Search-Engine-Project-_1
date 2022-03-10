import os.path
import requests
import pickle

from load import load_documents
import timing
from index import Index


# @timing
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)
        if i % 5000 == 0:
            print(f'Indexed {i} documents', end='\r')
    return index


if __name__ == '__main__':

    index = index_documents(load_documents(), Index())
    print(f'Index contains {len(index.documents)} documents')

    with open("data/index_dump-small.pickle", 'wb') as f:
        pickle.dump(index, f)

    index.search('London Beer Flood', search_type='AND')
    index.search('London Beer Flood', search_type='OR')
    index.search('London Beer Flood', search_type='AND', rank=True)
    index.search('London Beer Flood', search_type='OR', rank=True)
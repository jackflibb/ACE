""" Query PubMed for results from several journals, and save to file.
The resulting directory can then be passed to the Database instance for 
extraction, as in the create_db_and_add_articles example.
NOTE: selenium must be installed and working properly for this to work. 
Code has only been tested with the Chrome driver. """

import os
import sys
sys.path.append(os.getcwd())
from ace.scrape import *
import ace
from ace import database

# journals = {
#     'Neuroimage': {
#         'delay': 20,  # Mean delay between article downloads--prevents the banhammer
#         'mode': 'browser',  # ScienceDirect journals require selenium to work properly
#         'search': 'fmri',  # Only retrieve articles with this string in abstract
#         'min_pmid': 20000000   # Start from this PMID--can run incrementally
#     },

#     'PLoS ONE': {
#         'delay': 10,
#         'search': 'fmri',
#         'mode': 'direct',  # PLoS sends nice usable XML directly
#         'min_pmid': None
#     },
#     'Journal of Neuroscience': {
#         'delay': 20,
#         'mode': 'browser',
#         'search': 'fmri',
#         'min_pmid': None,
#         'limit': 100  # We can limit to only N new articles
#     }
# }

# Verbose output
ace.set_logging_level('debug')

# Create temporary output dir
output_dir = './tmp/articles'
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

# Initialize Scraper
scraper = Scraper(output_dir)

ids = [
"17427209",
"21966352",
"17475792",
"21300162",
"20188841",
"21382560",
"14960288",
"21232548",
"20809855",
"19651151",
"21686071",
"19875675",
"20816974",
"21782354",
"20933020",
"18586110",
"21499511",
"22137505",
"19766936",
"19580877"]

ids_designation='fixed_articles'

scraper.retrieve_journal_articles_by_id(ids,mode='direct',ids_designation=ids_designation,delay=1)

# Uncomment the next line to seem more information
ace.set_logging_level('debug')

# Change this to a valid path to a set of html files.
PATH_TO_FILES = output_dir + "/html/" + ids_designation + "/*.html"

meta_dir = './tmp/meta'
if not os.path.exists(meta_dir):
	os.makedirs(meta_dir)
table_dir = './tmp/table'
if not os.path.exists(table_dir):
	os.makedirs(table_dir)


db = database.Database(adapter='sqlite',db_name='sqlite:///example_db_test.sqlite')
db.add_articles(PATH_TO_FILES,pmid_filenames=True,metadata_dir=meta_dir,table_dir=table_dir)
db.print_stats()

db.save()
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

# ids = [
# "18345988",
# "15158422",
# "11969318",
# "21411661",
# "17427209",
# "14527602",
# "20188198",
# "19034055",
# "20625430",
# "21917846",
# "17986682",
# "15850746",
# "12874501",
# "17073981",
# "22194728",
# "22038344",
# "18452757",
# "21316467",
# "17979124",
# "17065463",
# "20200600",
# "18248824",
# "21738725",
# "20614370",
# "12899193",
# "22113088",
# "18971297",
# "20807576",
# "21966352",
# "18708149",
# "14531584",
# "17475792",
# "21300162",
# "21368210",
# "16793895",
# "20188841",
# "21127721",
# "21382560",
# "14960288",
# "16047521",
# "16942837",
# "21232548",
# "20934985",
# "20809855",
# "19651151",
# "18177676",
# "10654655",
# "9951219",
# "20502991",
# "20401808",
# "20215938",
# "21686071",
# "19875675",
# "18029095",
# "20816974",
# "11304075",
# "18281300",
# "21782354",
# "12244209",
# "17672385",
# "20035016",
# "18589507",
# "21196949",
# "18171363",
# "17118409",
# "21516542",
# "20933020",
# "18586110",
# "21499511",
# "22137505",
# "18422547",
# "19228430",
# "16683265",
# "21927631",
# "18185108",
# "18599179",
# "19766936",
# "17286837",
# "19580877",
# "15560325",
# "11209962",
# "21084608",
# "16775126",
# "15251900",
# "19812330",
# "18633805",
# "19406906"]

# ids_designation='1999_2011'

# ids = [
# "19228430"]

ids = [
"21183457",
"21828112",
"21917846",
"22033368",
"22228752",
"22484308",
"22569186",
"22768085",
"23106734",
"23127796",
"23202661",
"23245222",
"23376475",
"23511846",
"23544046",
"23586454",
"23707590",
"23832422",
"23845427",
"23959199",
"24033579",
"24071571",
"24309299",
"24513024",
"24553284",
"24558455",
"24651705",
"24920379",
"24971708",
"24971880"]

ids_designation='2012_2014'

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


db = database.Database(adapter='sqlite',db_name='sqlite:///example_db_2012.sqlite')
db.add_articles(PATH_TO_FILES,pmid_filenames=True,metadata_dir=meta_dir,table_dir=table_dir)
db.print_stats()

a_file = output_dir + "/html/" + ids_designation + "/14527602.html"
db.add_articles(a_file,pmid_filenames=True,metadata_dir=meta_dir,table_dir=table_dir)

db.save()


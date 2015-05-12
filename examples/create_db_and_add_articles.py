# In this example we create a new DB file and process a bunch of
# articles. Note that due to copyright restrictions, articles can't
# be included in this package, so you'll need to replace PATH_TO_FILES
# with something that works.

import ace
from ace import database
from ace import export
from ace.database import Database, Article, Table, Activation


# Uncomment the next line to seem more information
ace.set_logging_level('info')

# Change this to a valid path to a set of html files.
PATH_TO_FILES = "./tmp/articles/html/ids/*.html"

cd /home/jflournoy/Documents/NeuroDebian/code/metanal/ACE

db = database.Database('example_db.sqlite')
#db.add_articles(PATH_TO_FILES)
db.print_stats()


db.session.query(Article)


export.export_database(db,'exported_data.csv',groups=True)
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
cd /home/jflournoy/Documents/NeuroDebian/code/metanal/ACE
PATH_TO_FILES = "./tmp/articles/html/ids/*.html"

db = database.Database('example_db.sqlite')
#db.add_articles(PATH_TO_FILES)
db.print_stats()


export.export_database(db,'exported_data.csv',groups=True,size=True,statistic=True)

for article in db.session.query(Article).filter(Article.tables.any()).all():
	for t in article.tables:
		for p in t.activations:
			if isinstance(p.size, basestring):
                p.size_tmp = [p.size]
            elif p.size is None:
                p.size_tmp = []
            print(['///'.join(p.size_tmp).encode('utf-8')])

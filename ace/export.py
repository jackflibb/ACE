from database import Database, Article, Table, Activation
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)

def export_database(db, filename, metadata=True, groups=False, size=False, statistic=False):

    res = ['id\tdoi\tx\ty\tz\tspace\tpeak_id\ttable_id\ttable_num']

    if metadata:
    	res[0] += '\ttitle\tauthors\tyear\tjournal'

    if groups:
        res[0] += '\tgroups'
    if size:
        res[0] += '\tsize'
    if statistic:
        res[0] += '\tstatistic'

    articles = db.session.query(Article).filter(Article.tables.any()).all()
    for a in articles:
    	logger.info('Processing article %s...' % a.id)
        for t in a.tables:
            for p in t.activations:
                if t.number is None: t.number = ''
            	fields = [a.id, a.doi, p.x, p.y, p.z, a.space, p.id, t.id, t.number.strip('\t\r\n')]
            	if metadata:
            		fields += [a.title, a.authors, a.year, a.journal]
                if groups:
                    groups_tmp = []
                    if isinstance(p.groups, basestring):
                        groups_tmp = [p.groups]
                    elif p.groups is None:
                        groups_tmp = []
                    fields += ['///'.join(groups_tmp).encode('utf-8')]
                if size:
                    if isinstance(p.size, basestring):
                        size_tmp = [p.size]
                    elif p.size is None:
                        size_tmp = []
                    fields += ['///'.join(size_tmp).encode('utf-8')]
                if statistic:
                    if isinstance(p.statistic, basestring):
                        statistic_tmp = [p.statistic]
                    elif p.statistic is None:
                        statistic_tmp = []
                    fields += ['///'.join(statistic_tmp).encode('utf-8')]
                res.append('\t'.join(str(x) for x in fields))

    open(filename, 'w').write('\n'.join(res))
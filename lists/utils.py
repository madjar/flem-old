import datetime

def date_range(start, stop):
    for i in xrange(0, (stop - start).days):
        yield start + datetime.timedelta(i)

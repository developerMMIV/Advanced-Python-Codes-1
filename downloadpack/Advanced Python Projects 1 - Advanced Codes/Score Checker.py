def notes(*n, sit=False):
    '''

    :param n:
    :param sit:
    :return:
    '''

    r = dict()
    r['Total'] = len(n)
    r['Largest']= max(n)
    r['Smallest'] = min(n)
    r['Average']= sum(n)/len(n)
    if sit:
        if r['Average'] >= 7:
            r['Situation'] = "Great"
        elif r['Average']>=5:
            r['Situation']= 'Good'
        else:
            r['Situation']='Bad'

    return r

resp = notes(5.5,2.5,3.5,sit=True)
print(resp)
'''
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
'''

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs,**kargs):
    '''
    Total time to run func() reps times.
    Return (total time, last result)
    '''
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    '''
    Quickest func() among reps runs.
    Return (best time, last result)
    '''
    bst = float('inf')
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < bst: bst = elapsed
    return (bst, ret)

def best_of_total(reps1,reps2, func, *pargs,**kargs):
    '''
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    '''
    return bestof(reps1,total, reps2,func,*pargs,**kargs)

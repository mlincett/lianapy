'''
Auxiliary functions to histogram a discrete set of values.
Bins are centered on integers.
'''

def hist_discrete_aux(sample):
    lo, hi = np.min(sample), np.max(sample)
    r = (lo -0.5, hi +0.5)
    b = 1 + hi - lo
    return { 'range': r, 'bins': b }

def hist_discrete(ax, sample):
    return ax.hist(sample, **hist_discrete_aux(sample))

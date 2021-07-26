'''
Auxiliary functions to histogram a discrete set of values.
Bins are centered on integers.
'''

def hist_discrete_template(lo, hi):
    r = (lo -0.5, hi +0.5)
    b = 1 + hi - lo
    return { 'range': r, 'bins': b }

def hist_discrete_template_builder(sample):
    lo, hi = np.min(sample), np.max(sample)
    return hist_discrete_template(lo, hi)
    
def hist_discrete(data, template = None):
    if template is None:
        template = hist_discrete_template_builder(sample)
    return np.histogram(data, **template)
    
def draw_hist_discrete(ax, H, b):
    ax.bar(bins[:-1], H, width=1)
    
def hist_discrete_draw(ax, data):
    return ax.hist(data, **hist_discrete_template_builder(data))

def get_centers(edges):
    return (edges[1:] + edges[:-1]) / 2

def hist_to_graph(H):
    values, edges = H[0], H[1]
    return values, get_centers(edges)

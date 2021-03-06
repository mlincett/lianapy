import pandas as pd

def print_dict(D, n=0):
    ''' Print dictionary as a table exploiting pandas '''
    df = pd.DataFrame(D)
    print(df[n:].to_string(index=False))

''' HDF5 utilities '''

class TableMiner:
    '''
    Class to mine data from HDF5 data sets.
    A list of features is provided. Each features comes in the form of a feature name (for the output data), a table and a column to retrieve. 
    '''
    def __init__(self, features):
        self.features = features
    
    def mine(self, root):
        output = {}
        for feature in self.features:
            table, column, name = feature
            output[name] = root[table].col(column)
        return output
    
    def mine_to_df(self, root):
        return pd.DataFrame.from_dict(self.mine(root))
    
    def mine_to_hdf(self, root, filename, group='data', append=True):
        df = self.mine_to_df(root)
        df.to_hdf(filename, group, append=append) 

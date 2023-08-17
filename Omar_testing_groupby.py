import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal

# Testing groupby.rolling.corr, Pandas error reported on GitHub. Needs Testing
# Resolves Pandas GitHub #44078

# # Reported Test Cases

# df1 = pd.DataFrame({'a': [(1,), (1,), (1,)], 'b': [4, 5, 6]})
# gb1 = df1.groupby(['a'])

# df2 = pd.DataFrame({'a': [(1,2,), (1,2,), (1,2,)], 'b': [4, 5, 6]})
# gb2 = df2.groupby(['a'])


# # How to Create a DataFrame with the MultiIndex. Needed to create proper expected result variables

# index = pd.MultiIndex.from_tuples([((1,), 0), ((1,), 1), ((1,), 2)], names=['a',''])
# df = pd.DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [np.nan, 1.0, 1.0]}, index=index)
# print(df) 

# # Unit Test class 
class TestRollingCorrelation(unittest.TestCase):
    # Initialize test cases 
    def setUp(self):
        self.df1 = pd.DataFrame({'a': [(1,), (1,), (1,)], 'b': [4, 5, 6]})
        self.gb1 = self.df1.groupby(['a'])
         
        self.df2 = pd.DataFrame({'a': [(1, 2), (1, 2), (1, 2)], 'b': [4, 5, 6]})
        self.gb2 = self.df2.groupby(['a'])
    
    # Testing functions for variables initialized above

    # Test Case 1
    def test_rolling_corr_with_single_integer_in_index(self):
        result = (self.gb1.rolling(2).corr(other=self.df1))
        index = pd.MultiIndex.from_tuples([((1,), 0), ((1,), 1), ((1,), 2)], names=['a',None])
        expected = pd.DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [np.nan, 1.0, 1.0]}, index=index)
        # print(result)
        # print(expected)
        assert_frame_equal(result,expected)
    
    # Test Case 2
    def test_rolling_corr_with_tuples_in_index(self):
        result = (self.gb2.rolling(2).corr(other=self.df2))
        index = pd.MultiIndex.from_tuples([((1,2), 0), ((1,2), 1), ((1,2), 2)], names=['a',None])
        expected = pd.DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [np.nan, 1.0, 1.0]}, index=index)
        assert_frame_equal(result,expected)


if __name__ == '__main__':
    unittest.main()

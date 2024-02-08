# Parametrization for normalize_lc function testing
import pandas as pd
import lcanalyzer
import pytest
@pytest.mark.parametrize(
    "test_input_df, test_input_colname, expected",
    [
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, 4, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285])),
        (pd.DataFrame(data=[[1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.])),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
         pd.Series(data=[0.,0.,0.,0.])),
    ])
def test_normalize_lc(test_input_df, test_input_colname, expected):
    """Test how normalize_lc function works for arrays of positive integers."""
    from lcanalyzer.models import normalize_lc
    import pandas.testing as pdt
    pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)
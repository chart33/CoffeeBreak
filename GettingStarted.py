import pandas as pd
import numpy as np

def Test(n, cols):
	n_np_arr = np.asarray(n)
	n_df = pd.DataFrame(n_np_arr, columns = cols)

	print n_np_arr
	print n_df
	return n_df



test_arr = [[1,2,3],[4,5,6],[7,8,9]]
test_cols = ['A','B','C']

Test(test_arr, test_cols)



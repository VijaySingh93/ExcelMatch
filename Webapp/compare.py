import numpy as np
import pandas as pd

def xcel_compare(file1, file2):
    res = []
    try:
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)
    except Exception as e:
        error = (f'Encountered Exception: {e} '
              f'while reading files to DataFrame, '
              f'file1: {file1}, file2: {file2}')
        return error
    
    try:
        df1 = df1.fillna('')
        df2 = df2.fillna('')
    except Exception as e:
        error = (f'failed to strip nan from dataframes with exception : {e}')
        return error
    
    try:
        df1 == df2
    except Exception as e:
        error = (f'{file1} and {file2} do not contain same number of columns and rows')
        return error

    try:
        comparison_values = df1.values == df2.values
    except Exception as e:
        error = (f'Failed to compare dataframes with exception: {e}')
        return error

    try:
        rows, cols = np.where(comparison_values==False)
    except Exception as e:
        error = (f'Failed to generate Rows and Columns from comparison_values '
              f'with Exception: {e}')
        return error

    try:
        columns = df1.columns
        for item in zip(rows, cols):
            # df1.iloc[item[0], item[1]] = \
            #     f'{df1.iloc[item[0], item[1]]} --> ' \
            #     f'{df2.iloc[item[0], item[1]]}'
            res.append((item[0], item[1], str(df1.iloc[item[0], item[1]]), str(df2.iloc[item[0], item[1]])))
    except Exception as e:
        error = (f'Failed to get differences with exception: {e}')
        return error

    # try:
    #     # TODO: better output file (not ./)
    #     output_file = './Excel_diff.xlsx'
    #     df1.to_excel(output_file, index=False, header=True)
    #     print(f'Output resulting diff to: {output_file}')
    # except Exception as e:
    #     # TODO: add output filename to exception logging
    #     print(f'Failed to write to Excel file with exception: {e}')
    #     return

    return (res, columns)
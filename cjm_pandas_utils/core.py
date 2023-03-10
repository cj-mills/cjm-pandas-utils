# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['markdown_to_pandas', 'display_df']

# %% ../nbs/00_core.ipynb 3
import pandas as pd

# %% ../nbs/00_core.ipynb 4
def markdown_to_pandas(md_table_str:str): # The markdown table string to be converted.
    """
    Convert a markdown table string to a pandas DataFrame.
    """
    
    # Split the input markdown string into separate lines
    lines = md_table_str.strip().split("\n")
    
    # Split the first line of the input markdown string into columns
    columns = lines[0].split("|")[1:-1]
    
    # Strip the whitespaces in the columns
    columns = [x.strip() for x in columns]
    
    # Split the remaining lines of the input markdown string into rows of data
    data = [line.split("|")[1:-1] for line in lines[2:]]
    
    # Strip the whitespaces in each row of data
    data = [[x.strip() for x in row] for row in data]
    
    # Create a pandas DataFrame from the columns and data
    return pd.DataFrame(data, columns=columns)

# %% ../nbs/00_core.ipynb 8
def display_df(df:pd.DataFrame, # The DataFrame to be displayed.
               align:str='left'): # Alignment for the headers and all the cells.
    """
    Display a pandas DataFrame with specified alignment for the headers and all the cells.
    """
    # Set the properties for the styler object
    properties = {'width': 'auto', 'text-align': align}
    
    # Set the styles for the table
    styles = [{'selector': 'th', 'props': [('text-align', align)]}]
    
    # Return the styler object with set properties and table styles
    return df.style.set_properties(**properties).set_table_styles(styles)

import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Parsing error: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

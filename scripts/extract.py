import pandas as pd 


def read_file(file_path):
    try:
        # Assuming the input file is a CSV
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return None
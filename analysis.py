import pandas as pd

def run_analysis():
    try:
        # Load data
        data = pd.read_csv('data/sample.csv')
        
        # Perform analysis (e.g., calculate mean)
        mean_value = data['value'].mean()

        return {'mean': mean_value}
    except Exception as e:
        print(f"Error in run_analysis: {e}")
        return {'mean': 'Error'}



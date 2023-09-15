import pandas as pd

def is_all_pass(data: pd.DataFrame) -> bool:
    return (data['Result']=='Pass').all()

def get_only_passes(data: pd.DataFrame) -> pd.DataFrame:
    return data[data['Result']=='Pass'].reset_index(drop=True)
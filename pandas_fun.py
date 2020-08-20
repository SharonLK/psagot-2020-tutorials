import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('resources/got-character-deaths.csv')

    print(df.head())
    print('=' * 100)
    print(df.columns)
    print('=' * 100)
    print(df.describe())

    # TODO: Have more fun with pandas

def main():
    import pandas as pd 
    file = input().strip()
    func = input().strip()

    df = pd.read_csv(file)

    if func == 'Q1':
        # Do something
        print(df.shape)
    elif func == 'Q2':
        # Do something
        print(df['score'].max())
    elif func == 'Q3':
        # Do something
        condition = df['score'] > 80
        print( df[condition]['id'].count())
    else:
        # Do something
        print("No Output")

if __name__ == "__main__":
    main()
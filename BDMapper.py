import pandas as pd
from operator import itemgetter


def mapper():

    data = pd.read_csv('original-tic-tac-toe.data')
    convert = []

    for index, row in data.iterrows():
        for position in data.columns[:-1]:

            if row.loc[position] == 'x':
                if row.loc['class'] == 'positive':
                    convert.append(f'{position},P')
                else:
                    convert.append(f'{position},N')

    convert.sort(key=itemgetter(4, 0), reverse=True)

    # print(convert)
    return convert


# mapper()

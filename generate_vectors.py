import pandas as pd
import numpy as np


OUTPUT_FILENAME = 'vectors.csv'

N_INTERVAL = (500, 1000)
M_INTERVAL = (10, 50)
VAL_INTERVAL = (-1, 1)

N_DEFAULT = 750
M_DEFAULT = 30

def is_in_interval(num, interval: tuple):
    return (interval[0]<num)&(num<=interval[1])

def generate_vectors(N, M) -> pd.DataFrame:
    df = pd.DataFrame(np.random.uniform(*VAL_INTERVAL,size=(N, M)))
    return df

def main():
    n = int(input('Введите 500<N≤1000: ') or N_DEFAULT)
    assert is_in_interval(n, N_INTERVAL), 'N выходит за пределы интервала 500<N≤1000'
    m = int(input('Введите 10<m≤50: ') or M_DEFAULT)
    assert is_in_interval(m, M_INTERVAL), 'm выходит за пределы интервала 10<m≤50'

    df = generate_vectors(n, m)

    df.to_csv(OUTPUT_FILENAME, sep=',', header=False, index=False)

    print(f'Создан файл {OUTPUT_FILENAME}. N = {n}, M = {m}. С числами в интервале [{VAL_INTERVAL[0]}, {VAL_INTERVAL[1]})')

if __name__ == '__main__':
    main()
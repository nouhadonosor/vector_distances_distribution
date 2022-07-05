import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import cdist

INPUT_FILENAME = 'vectors.csv'
PLOT_X_INTERVAL = (0, 100)
PLOT_Y_TICKS_INTERVAL = (0, 5)
PLOT_Y_TICKS_STEP = 0.1

def get_vectors_df(filename=INPUT_FILENAME):
    return pd.read_csv(
        filename,
        sep=',',
        header=None, 
        index_col=False
    )

def main():
    df = get_vectors_df()
    dfdms = pd.DataFrame(cdist(df,df, 'euclid')).stack()
    dfdms = dfdms[dfdms.index.get_level_values(0) != dfdms.index.get_level_values(1)]
    print(f'Максимальное расстояние {float(dfdms.max())} у векторов {dfdms.idxmax()}')
    print(f'Минимальное расстояние {float(dfdms.min())} у векторов {dfdms.idxmin()}')
    dfdms[slice(*PLOT_X_INTERVAL)].plot(
        kind = "bar",
        yticks=np.arange(*PLOT_Y_TICKS_INTERVAL, PLOT_Y_TICKS_STEP),
        figsize=(25,10)
    )
    plt.show()
    

if __name__ == '__main__':
    main()
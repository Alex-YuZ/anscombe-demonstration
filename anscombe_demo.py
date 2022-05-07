import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('anscombe.csv')

def generate_equation(x, y):
    slope, intercept = np.polyfit(x, y, deg=1)
    eq_str = """
    y = {:.2f}*x + {:.2f}
    """
    return eq_str.format(slope, intercept)

ansc_np = df.to_numpy().flatten(order='F').reshape(2, 2, 2, 11)

fig, ax = plt.subplots(2, 2, sharex='all', sharey='all', figsize=(15, 10))
fig.subplots_adjust(hspace=.05, wspace=.05, top=.93)
fig.suptitle("Anscomb's Quartet", fontsize=15, fontweight='bold')
for row in range(2):
    for col in range(2):
        sns.regplot(x=ansc_np[row, col][0], 
                    y=ansc_np[row, col][1], 
                    ci=None, 
                    line_kws={'color': 'red', 'linewidth': 1}, 
                    ax=ax[row, col], truncate=False);
        ax[row, col].text(14, 9, generate_equation(ansc_np[row, col][0], ansc_np[row, col][1]), 
                          fontdict={'size':12}, color='blue')
        
ax[0,0].set_ylabel('Y', rotation=0, fontweight='bold')
ax[1,0].set_ylabel('Y', rotation=0, fontweight='bold')
ax[1,0].set_xlabel('X', fontweight='bold')
ax[1,1].set_xlabel('X', fontweight='bold');

plt.show()
fig.savefig('Anscombe_Viz.jpg')
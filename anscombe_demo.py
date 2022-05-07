from matplotlib import docstring
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from csv file
df = pd.read_csv('anscombe.csv')

def generate_equation(x, y):
    """Add formula text on plots

    Args:
        x (numpy.array): data on the x-axis
        y (numpy.array): data on the y-axis

    Returns:
        str: formatted linear equation string
    """    """"""
    
    slope, intercept = np.polyfit(x, y, deg=1)
    eq_str = """
    y = {:.2f}*x + {:.2f}
    """
    return eq_str.format(slope, intercept)

# Reconstruct df to numpy arrays to 2*2*2*11 shape
ansc_np = df.to_numpy().flatten(order='F').reshape(2, 2, 2, 11)

# Add subplots object
fig, ax = plt.subplots(2, 2, sharex='all', sharey='all', figsize=(15, 10))

# Adjust general subplots properties
fig.subplots_adjust(hspace=.05, wspace=.05, top=.93)
fig.suptitle("Anscomb's Quartet", fontsize=15, fontweight='bold')

# Plot each regplot
for row in range(2):
    for col in range(2):
        sns.regplot(x=ansc_np[row, col][0], 
                    y=ansc_np[row, col][1], 
                    ci=None, 
                    line_kws={'color': 'red', 'linewidth': 1}, 
                    ax=ax[row, col], truncate=False);
        ax[row, col].text(14, 9, generate_equation(ansc_np[row, col][0], ansc_np[row, col][1]), 
                          fontdict={'size':12}, color='blue')

# Customize certain x and y labels        
ax[0,0].set_ylabel('Y', rotation=0, fontweight='bold')
ax[1,0].set_ylabel('Y', rotation=0, fontweight='bold')
ax[1,0].set_xlabel('X', fontweight='bold')
ax[1,1].set_xlabel('X', fontweight='bold');

# Display the result and save it!
plt.show()
fig.savefig('Anscombe_Viz.jpg')
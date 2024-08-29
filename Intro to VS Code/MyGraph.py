import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
# Step one create a virtural enviornemnt 
#python3-m venv (myvenv) <can be named anything 
# Step 2 activate your virtural enviornment 
#source myvenv/bin/activate
# Step 3 Istall 3rd party library 
import control
import matplotlib.pyplot as plt

#%%
sys = control.tf([1, 2], [2, 4, 1])

t, y = control.step_response(sys)

plt.plot(t, y)
plt.show()
#%%

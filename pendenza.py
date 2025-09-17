# %% [markdown]
# # Pendenza di una curva

# %% [markdown]
# ## Importazione delle librerie necessarie

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## Definizione della funzione
# 
# $$ f(x)=2x^3-x^2-3x+1 $$

# %%
def f(x):
    return(x**3+x**2-5*x+1)


# %%
f(0)

# %%
x=np.linspace(-10,10,201)
print(x)

# %%
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafico di f(x)')
plt.grid(True)
plt.ylim(-10, 10)
plt.show()

# %%
def m(x):
    dx=1e-6
    return((f(x+dx)-f(x))/dx)

# %%
plt.plot(x, f(x))
plt.plot(x, m(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafico di f(x)')
plt.grid(True)
plt.ylim(-10, 10)
plt.show()

# %%
from scipy.interpolate import interp1d

# Interpolazione quadratica di m(x)
interp_m = interp1d(x, m(x), kind='quadratic')

# Esempio: calcolo valori interpolati su una griglia più fine
x_fine = np.linspace(-10, 10, 1001)
m_interp = interp_m(x_fine)

plt.plot(x, m(x), label='m(x) originale')
plt.plot(x_fine, m_interp, label='Interpolazione quadratica', linestyle='--')
plt.xlabel('x')
plt.ylabel('m(x)')
plt.legend()
plt.grid(True)
plt.show()

# %%
# I coefficienti dell'interpolazione quadratica non sono direttamente accessibili tramite interp1d,
# perché interp1d costruisce una funzione interpolante, non restituisce i coefficienti dei polinomi locali.
# Se vuoi i coefficienti di interpolazione polinomiale globale, puoi usare np.polyfit:

coeffs = np.polyfit(x, m(x), 2)
print("Coefficienti della parabola globale:", coeffs)

# %%
coeffs_rounded = np.round(coeffs, 4)
print("Coefficienti arrotondati a 4 cifre significative:", coeffs_rounded)



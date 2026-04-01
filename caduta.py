# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
t0=0.0
dt=0.00001
dt_tab=0.5
tf=4.8
g=9.81
y0=100.0
v0=0.0
n=int((tf-t0)/dt_tab+1)
tabella=np.zeros((n,4))
print(tabella.shape)

t=t0
t_tab=0.0
y=y0
v=v0
i=0
while t<=tf:
    if t_tab>= dt_tab:
        tabella[i,0]=t
        tabella[i,1]=y
        tabella[i,2]=v
        tabella[i,3]=-0.5*g*t**2+y0
        t_tab=0.0
        i=i+1
    v=v-g*dt
    y=y+v*dt
    t=t+dt
    t_tab=t_tab+dt

tabella = tabella[:i]

#plt.plot(tabella[:,0],tabella[:,1])
#plt.plot(tabella[:,0],tabella[:,3])


    



# %%
print (tabella)

intestazione = "t y v a"
np.savetxt('tabella.csv', tabella, header=intestazione, comments='', fmt='%10.5f')



# %%
nome_file = "tabella.tex"

with open(nome_file, "w") as f:
    # Intestazione della tabella
    # (r"testo") è una stringa raw, che permette di scrivere \ senza doverlo raddoppiare
    f.write(r"\begin{tabular}{S[table-format=1.1] S[table-format=2.3] S[table-format=2.3] S[table-format=2.3]}" + "\n")
    f.write(r"\toprule" + "\n")
    f.write(r"$t$ & $y$ & $v$ & $a$ \\" + "\n")
    f.write(r"\midrule" + "\n")

    # Ciclo di scrittura dati
    for i in range(len(tabella)):
        # Estraiamo i valori per chiarezza
        t, y, v, a = tabella[i, 0], tabella[i, 1], tabella[i, 2], tabella[i, 3]
        
        # Formattazione: 1.4f significa 1 cifra intera e 4 decimali
        # L'id i è un intero, gli altri sono float
        # (f"testo") è una stringa formattata, il \ deve essere raddoppiato
        riga = f"{t:1.1f} & {y:2.3f} & {v:2.3f} & {a:3.3f} \\\\" + "\n"
        f.write(riga)

    # Chiusura tabella
    f.write(r"\bottomrule" + "\n")
    f.write(r"\end{tabular}" + "\n")
    
    f.write("\n")
    
    f.write(r"% valore limite in m/s" + "\n")
    vlim = abs(np.min(tabella[:,2]))
    f.write(r"\newcommand\vlim{")
    f.write(f"{vlim:.1f}")
    f.write(r"}" + "\n\n")

    f.write(r"% valore limite in km/h" + "\n")
    vlimkmh = vlim*3.6  # Conversione in km/h
    f.write(r"\newcommand\vlimkmh{")
    f.write(f"{vlimkmh:.0f}")
    f.write(r"}" + "\n")



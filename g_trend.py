import numpy as np
import pandas 
import random
from classy import Class
from scipy import interpolate as int

df_lab = pandas.read_csv("chain.paramnames", usecols=([0]), header=None, delim_whitespace=1, names=(["labels"]) )
labels = list(df_lab["labels"].values)
labels.insert(0, "loglik")
labels.insert(0, "wt")
df = pandas.read_csv("chain_1.txt", header=None, names=labels, delim_whitespace=1)

lcdm = Class()
lcdm.set({
        'h': df["H0*"].values[i]/100.0,
        'omega_b': df.omegabh2.values[i],
        'omega_cdm': df.omegach2.values[i],
        'Omega_Lambda': 0.,
        'w0_fld': -1.0,
        'wa_fld': 0.0,
        'background_verbose':1,
        'input_verbose':1,
        'gauge':'Newtonian',
})

lcdm.compute()

b = lcdm.get_background()
x = b["comov. dist"]
z = b["xz"]
Chi = int.interpd1(z,x)
Z_s = 0.8
Z = 0.4
Chi_s = Chi(Z_s)
Chi_z = Chi(Z)

Omega_m = np.mean(df["omegach2"].values)
H0 = np.mean(df["H0"].values)
sigma8 = np.mean(df["sigma8*"].values)

for x in range(10000):
    a[i] = random.uniform(0.5,1.6,size=5)
 
fout = open("best_fit_para.txt","w")
fout.write("%.3f" % a)
fout.write("\n")

for i in range(a.):
  
                      BCP[i] =  Omega_m**(a)*sigma8**(b)*H0**(2*c)*((Chi_z*(1+Z_s)/(Chi_s*(1+Z)))-1)**d*(lcdm.scale_independent_growth_factor(Z))**e*(1+Z)**2
                      fout.write("%.4f" % BCP[i])
                      fout.write("\n")
                      break                  

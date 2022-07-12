import matplotlib as mpl
mpl.use('TkAgg')
from qwind import wind
from qwind import constants
import matplotlib.pyplot as plt
from qwind import utils
import time

time_s=time.time()
rho=5e7
m=1e8
dot=0.2
R=3000
example = wind.Qwind(M=m,mdot=dot,lines_r_min =20, lines_r_max=R,disk_r_max=R, f_x=0.1, rho_shielding=rho,nr=40,T=25e3)

#for key in example.lines._dict_.keys():
#    if 'hist' in key:
#        print(key)
#fig=plt.figure(1)
#ax1=plt.subplot(1,2,1)
example.start_lines(v_z_0=1e7,rho_0=rho)
#for line in example.lines:
#    plt.plot(line.r_hist, line.z_hist)
#plt.xlabel("R [Rg]")
#plt.ylabel("z [Rg]")
#ax2=plt.subplot(1,2,2)
#for line in example.lines:
#   plt.plot(line.r_hist,line.v_z_hist)
#plt.xlabel("R [Rg]")
#plt.ylabel("v_z [C]")
#plt.savefig('fx={},T0={},rho={},vz={}的流线图'.format(fx,T0,rho,vz))
time_e=time.time()
print('total time',time_e-time_s)
#plt.show()
utils.save_results(example, "B3_nr40")
#print(example.mdot_w) # units of g/s

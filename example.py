import matplotlib as mpl
mpl.use('TkAgg')
from qwind import wind
from qwind import constants
import matplotlib.pyplot as plt
from qwind import utils
import time
#r_min =eval(input('请输入最小半径：'))
#r_max =eval(input('请输入最大半径：'))
#fx=eval(input('请输入x射线占比：'))
#rhoshielding=eval(input('请输入初始密度：'))
#n=eval(input('请输入流线条数：'))
#T0=eval(input('请输入温度：'))
#vz=eval(input('请输入初始速度：'))
#rho=eval(input('请输入流线初始密度:'))
#example = wind.Qwind(lines_r_min =r_min, lines_r_max=r_max, f_x=fx, rho_shielding=rhoshielding,nr=n,T=T0)
#line = example.line(r_0 = 150, rho_0 = 1e10, v_z_0 = 1e7,max_iter=1000)
#line.iterate()
#plt.plot(line.r_hist, line.z_hist)
#plt.xlabel("R [Rg]")
#plt.ylabel("z [Rg]")
#plt.show()
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

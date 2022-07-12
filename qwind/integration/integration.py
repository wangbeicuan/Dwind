import os
from math import*
import numpy as np
from qwind import constants
from ctypes import *
from scipy import LowLevelCallable
from scipy import integrate
from numpy.ctypeslib import ndpointer
c_double_p = POINTER(c_double)

class Parameters(Structure):
    _fields_ = [("r", c_double),
            ("z", c_double),
            ("r_d", c_double),
            ("R_g", c_double),
            ("astar", c_double),
            ("isco", c_double),
            ("r_min", c_double),
            ("r_max", c_double),
           ("epsabs", c_double),
            ("epsrel", c_double),
            ]



library_path = os.path.dirname(__file__)
#
lib_1 = CDLL(os.path.join(library_path, "qwind_radiation.so"))
lib_2 = CDLL(os.path.join(library_path, "energy.so"))
lib_3 = CDLL(os.path.join(library_path, "prr.so"))
lib_4 = CDLL(os.path.join(library_path, "prphi.so"))
lib_5 = CDLL(os.path.join(library_path, "prz.so"))
lib_6 = CDLL(os.path.join(library_path, "pphiphi.so"))
lib_7 = CDLL(os.path.join(library_path, "pphiz.so"))
lib_8 = CDLL(os.path.join(library_path, "pzz.so"))

#radiation
nt_rel_factors = lib_1.nt_rel_factors
nt_rel_factors.restype = c_double
nt_rel_factors.argtypes = (c_double, c_double, c_double)

workspace_initializer = lib_1.initialize_integrators

integrate_simplesed_r = lib_1.integrate_simplesed_r
integrate_simplesed_r.restype = c_double
integrate_simplesed_r.argtypes = [POINTER(Parameters)]

integrate_simplesed_z = lib_1.integrate_simplesed_z
integrate_simplesed_z.restype = c_double
integrate_simplesed_z.argtypes = [POINTER(Parameters)]

integrate_simplesed_phi = lib_1.integrate_simplesed_phi
integrate_simplesed_phi.restype = c_double
integrate_simplesed_phi.argtypes = [POINTER(Parameters)]
#energy
e_nt_rel_factors = lib_2.nt_rel_factors
e_nt_rel_factors.restype = c_double
e_nt_rel_factors.argtypes = (c_double, c_double, c_double)

e_workspace_initializer = lib_2.initialize_integrators

e_integrate_simplesed_z = lib_2.integrate_simplesed_z
e_integrate_simplesed_z.restype = c_double
e_integrate_simplesed_z.argtypes = [POINTER(Parameters)]
#p_rr
p_rr_nt_rel_factors = lib_3.nt_rel_factors
p_rr_nt_rel_factors.restype = c_double
p_rr_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_rr_workspace_initializer = lib_3.initialize_integrators

p_rr_integrate_simplesed_z = lib_3.integrate_simplesed_z
p_rr_integrate_simplesed_z.restype = c_double
p_rr_integrate_simplesed_z.argtypes = [POINTER(Parameters)]
#p_r_phi
p_rphi_nt_rel_factors = lib_4.nt_rel_factors
p_rphi_nt_rel_factors.restype = c_double
p_rphi_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_rphi_workspace_initializer = lib_4.initialize_integrators

p_rphi_integrate_simplesed_z = lib_4.integrate_simplesed_z
p_rphi_integrate_simplesed_z.restype = c_double
p_rphi_integrate_simplesed_z.argtypes = [POINTER(Parameters)]
#p_rz
p_rz_nt_rel_factors = lib_5.nt_rel_factors
p_rz_nt_rel_factors.restype = c_double
p_rz_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_rz_workspace_initializer = lib_5.initialize_integrators

p_rz_integrate_simplesed_z = lib_5.integrate_simplesed_z
p_rz_integrate_simplesed_z.restype = c_double
p_rz_integrate_simplesed_z.argtypes = [POINTER(Parameters)]

#p_phiphi
p_phiphi_nt_rel_factors = lib_6.nt_rel_factors
p_phiphi_nt_rel_factors.restype = c_double
p_phiphi_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_phiphi_workspace_initializer = lib_6.initialize_integrators

p_phiphi_integrate_simplesed_z = lib_6.integrate_simplesed_z
p_phiphi_integrate_simplesed_z.restype = c_double
p_phiphi_integrate_simplesed_z.argtypes = [POINTER(Parameters)]
#p_phiz
p_phiz_nt_rel_factors = lib_7.nt_rel_factors
p_phiz_nt_rel_factors.restype = c_double
p_phiz_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_phiz_workspace_initializer = lib_7.initialize_integrators

p_phiz_integrate_simplesed_z = lib_7.integrate_simplesed_z
p_phiz_integrate_simplesed_z.restype = c_double
p_phiz_integrate_simplesed_z.argtypes = [POINTER(Parameters)]
#p_zz
p_zz_nt_rel_factors = lib_8.nt_rel_factors
p_zz_nt_rel_factors.restype = c_double
p_zz_nt_rel_factors.argtypes = (c_double, c_double, c_double)

p_zz_workspace_initializer = lib_8.initialize_integrators

p_zz_integrate_simplesed_z = lib_8.integrate_simplesed_z
p_zz_integrate_simplesed_z.restype = c_double
p_zz_integrate_simplesed_z.argtypes = [POINTER(Parameters)]



class IntegratorSimplesed:

    def __init__(self,
            Rg,
            r_min = 6.,
            r_max = 1600.,
            epsabs=0,
            epsrel=1e-4,
            astar =0.,
            isco = 6.):
        self.Rg=Rg
        self.r_min=r_min
        self.r_max =r_max
        self.astar =astar
        self.isco =isco
        
        self.params = Parameters(
                r = 0.,
                z = 0.,
                r_d = 0.,
                R_g = Rg,
                astar = astar,
                isco = isco,
                r_min = r_min,
                r_max = r_max,
                epsabs = epsabs,
                epsrel = epsrel,
                )
        workspace_initializer()
        e_workspace_initializer()
        p_rr_workspace_initializer()
        p_phiphi_workspace_initializer()
        p_zz_workspace_initializer()
        p_rphi_workspace_initializer()
        p_rz_workspace_initializer()
        p_phiz_workspace_initializer()
    def integrate_radiation(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = integrate_simplesed_r(byref(self.params))
        z_int = integrate_simplesed_z(byref(self.params))
        phi_int=integrate_simplesed_phi(byref(self.params))#phi
        return [r_int,phi_int, z_int]
    def integrate_energy(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = e_integrate_simplesed_z(byref(self.params))#phi
        return [r_int,r_int, r_int]
    def integrate_p_rr(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_rr_integrate_simplesed_z(byref(self.params))
        return [r_int]
    def integrate_p_rphi(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_rphi_integrate_simplesed_z(byref(self.params))
        return [r_int]
    def integrate_p_rz(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_rz_integrate_simplesed_z(byref(self.params))
        return [r_int]

    def integrate_p_phiphi(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_phiphi_integrate_simplesed_z(byref(self.params))
        return [r_int]
    def integrate_p_phiz(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_phiz_integrate_simplesed_z(byref(self.params))
        return [r_int]

    def integrate_p_zz(self, r, z):
        self.params.r = r
        self.params.z = z
        r_int = p_zz_integrate_simplesed_z(byref(self.params))
        return [r_int]


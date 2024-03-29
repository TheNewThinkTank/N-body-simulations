
import h5py
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# from general.bin_halo import bin_halo_radially
from modulus import modulus  # type: ignore

user_path = Path.cwd()
desktop_path = user_path / "Desktop/"
GADGET_E_path = desktop_path / "RunGadget/Energy_Exchange/"
stable_path = "Energy_exchange/Stable_structures/"
figure_path = desktop_path / stable_path / "figures/"

R_middle = 0

sims = ["Soft_B", "CS1", "CS4", "CS5", "CS6", "DS1", "Soft_D2", "E"]
# text_files_path = Desktop_path / Stable_path / 'text_files/' + sims[0] + 'E/'

Soft_B_path = "E_HQ_1000000_B/output/"
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_0_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_1_000.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + Soft_B_path + 'B_E_G2P_20_005.hdf5'
CS1_path = "E_HQ_10000_CS1/output/"
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS1_path + 'B_E_G2P_20_005.hdf5'
CS4_path = "E_HQ_100000_CS4/output/"
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_19_005.hdf5'
# Filename = GADGET_E_path + 'E_HQ_100000_CS4/' + 'B_E_19_005_P2G.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_20_000.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + CS4_path + 'B_E_G2P_30_005.hdf5'
CS5_path = "E_HQ_100000_CS5/output/"
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS5_path + 'B_E_G2P_20_005.hdf5'
CS6_path = "E_HQ_100000_CS6/output/"
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + CS6_path + 'B_E_G2P_30_005.hdf5'
DS1_path = "E_0_5_100000_DS1/output/"
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + DS1_path + 'B_E_G2P_30_005.hdf5'
Soft_D2_path = "E_0_5_100000_D2/output/"
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_20_005.hdf5'
# Filename = GADGET_E_path + Soft_D2_path + 'B_E_G2P_30_005.hdf5'
E_path = "E_HQ_1000000_E/output/"
# Filename = GADGET_E_path + E_path + 'B_E_G2P_0_000.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_2_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_4_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_6_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_8_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_10_005.hdf5'
# Filename = GADGET_E_path + E_path + 'B_E_G2P_20_005.hdf5'

# Control
con_Soft_B_path = "E_HQ_1000000_B_control/output/"
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_10_005.hdf5'
# Filename = GADGET_E_path + con_Soft_B_path + 'B_E_20_005.hdf5'
con_CS1_path = "E_HQ_10000_CS1_control/output/"
# Filename = GADGET_E_path + con_CS1_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS1_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS1_path + 'B_E_20_005.hdf5'
con_CS4_path = "E_HQ_100000_CS4_control/output/"
# Filename = GADGET_E_path + con_CS4_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS4_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS4_path + 'B_E_20_005.hdf5'
con_CS5_path = "E_HQ_100000_CS5_control/output/"
# Filename = GADGET_E_path + con_CS5_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS5_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS5_path + 'B_E_20_005.hdf5'
con_CS6_path = "E_HQ_100000_CS6_control/output/"
# Filename = GADGET_E_path + con_CS6_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_CS6_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_CS6_path + 'B_E_20_005.hdf5'
con_DS1_path = "E_0_5_100000_DS1_control/output/"
# Filename = GADGET_E_path + con_DS1_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_DS1_path + 'B_E_0_001.hdf5'
Filename = GADGET_E_path / con_DS1_path / "B_E_20_005.hdf5"
con_Soft_D2_path = "E_0_5_100000_D2_control/output/"
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_Soft_D2_path + 'B_E_20_005.hdf5'
con_E_path = "E_HQ_1000000_E_control/output/"
# Filename = GADGET_E_path + con_E_path + 'B_E_0_000.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_0_001.hdf5'
# Filename = GADGET_E_path + con_E_path + 'B_E_20_005.hdf5'

SnapshotFile = h5py.File(Filename, "r")
# F = 'Soft_B' + Filename[len(GADGET_E_path + Soft_B_path + 'B'):-5]
# F = 'Soft_B' + Filename[len(GADGET_E_path + con_Soft_B_path + 'B'):-5]
# F = 'CS1' + Filename[len(GADGET_E_path + CS1_path + 'B'):-5]
# F = 'CS1' + Filename[len(GADGET_E_path + con_CS1_path + 'B'):-5]
# F = 'CS4' + Filename[len(GADGET_E_path + CS4_path + 'B'):-5]
# F = 'CS4' + Filename[len(GADGET_E_path + con_CS4_path + 'B'):-5]
# F = 'CS5' + Filename[len(GADGET_E_path + CS5_path + 'B'):-5]
# F = 'CS5' + Filename[len(GADGET_E_path + con_CS5_path + 'B'):-5]
# F = 'CS6' + Filename[len(GADGET_E_path + CS6_path + 'B'):-5]
# F = 'CS6' + Filename[len(GADGET_E_path + con_CS6_path + 'B'):-5]
# F = 'DS1' + Filename[len(GADGET_E_path + DS1_path + 'B'):-5]
# F = 'DS1' + Filename[len(GADGET_E_path + con_DS1_path + 'B'):-5]
# F = 'Soft_D2'+ Filename[len(GADGET_E_path + Soft_D2_path + 'B'):-5]
# F = 'Soft_D2'+ Filename[len(GADGET_E_path + con_Soft_D2_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + E_path + 'B'):-5]
# F = 'E' + Filename[len(GADGET_E_path + con_E_path + 'B'):-5]

Gamma = -3.0
Beta = 1.0

new_R_middle = 0
R_bin_automatic = 0

Fig_v_logr = 0
Fig_v_logr_r2 = 0
Fig_x_hist = 0
Fig_x_hist2d = 0
Fig1_xy_xz = 0
Fig2_v = 0
Fig3_sigma = 0
Fig3_sigma_r_2 = 0
Fig3_sigma_divided_by_v_circ_r_2 = 0

Fig4_beta = 0
Fig4_beta_r_2 = 0
Fig5_kappa = 0
Fig5_kappa_r_2 = 0
Fig6_gamma = 0
Fig6_gamma_r_2 = 0
Fig7_betagamma = 0

save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho = 0

bins_202 = 0
bins_102 = 0
bins_52 = 0
bins_22 = 0

R_limit_10000 = 0
R_limit_5000 = 0
R_limit_50 = 0
R_limit_32 = 0

# if keep_IC_R_middle:  # For R_limit_10000, 20 bins.
#     if F.startswith(("Hernquist10000_G", "OsipkovMerritt_")):
#         # Dict: {key=Gamma: value=R_middle}
#         Dict = {-1.5: 0, -2.0: 0, -2.5: 0, -3.0: 0}

if new_R_middle:  # Choose new R_middle for each file.
    RmiddleOnes = {-1.5: 1, -2.0: 1, -2.5: 1, -3.0: 1}
    # List of tuples with string and dict of Gamma and Rmiddle, [('filename', {Gamma_1: R_middle_1, ..., Gamma_4: R_middle_4})]

    Gamma_Rmiddle_list = [
        ("B_E_G2P_0_000", RmiddleOnes),
        ("B_E_G2P_20_005", RmiddleOnes),
        (
            "B_E_0_000",
            {-1.5: 10**-0.7, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        (
            "B_E_0_001",
            {-1.5: 10**-0.7, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        (
            "B_E_20_005",
            {-1.5: 10**-0.6, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        ("CS1_E_G2P_0_000", RmiddleOnes),
        (
            "CS4_E_G2P_0_000",
            {-1.5: 10**-0.65, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.3},
        ),
        (
            "CS4_E_G2P_2_005",
            {-1.5: 10**-0.52, -2.0: 10**-0.3, -2.5: 10**0.05, -3.0: 10**0.3},
        ),
        (
            "CS4_E_G2P_4_005",
            {-1.5: 10**-0.52, -2.0: 10**-0.25, -2.5: 10**0.05, -3.0: 10**0.27},
        ),
        (
            "CS4_E_G2P_6_005",
            {-1.5: 10**-0.48, -2.0: 10**-0.25, -2.5: 1.0, -3.0: 10**0.27},
        ),
        ("CS4_E_G2P_8_005", RmiddleOnes),
        ("CS4_E_G2P_10_005", RmiddleOnes),
        (
            "CS4_E_G2P_20_005",
            {-1.5: 10**-0.45, -2.0: 10**-0.25, -2.5: 10**-0.05, -3.0: 10**0.25},
        ),
        (
            "CS4_E_20_005",
            {-1.5: 10**-0.4, -2.0: 10**-0.23, -2.5: 10**-0.05, -3.0: 10**0.25},
        ),
        (
            "CS5_E_G2P_0_000",
            {-1.5: 10**-0.7, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.38},
        ),
        (
            "CS5_E_G2P_2_005",
            {-1.5: 10**-0.6, -2.0: 10**-0.3, -2.5: 10**-0.1, -3.0: 10**0.3},
        ),
        (
            "CS5_E_G2P_4_005",
            {-1.5: 10**-0.55, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.35},
        ),
        (
            "CS5_E_G2P_6_005",
            {-1.5: 10**-0.48, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.3},
        ),
        ("CS5_E_G2P_8_005", RmiddleOnes),
        ("CS5_E_G2P_10_005", RmiddleOnes),
        (
            "CS5_E_G2P_20_005",
            {
                -1.5: 10**-0.42,
                -2.0: 10**-0.25,
                -2.5: 10**-0.05,
                -3.0: 10**-0.28,
            },
        ),
        (
            "CS5_E_20_005",
            {-1.5: 10**-0.45, -2.0: 10**-0.23, -2.5: 10**-0.04, -3.0: 10**0.3},
        ),
        (
            "CS6_E_G2P_0_000",
            {-1.5: 10**-0.73, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.34},
        ),
        (
            "CS6_E_G2P_2_005",
            {-1.5: 10**-0.55, -2.0: 10**-0.3, -2.5: 1.0, -3.0: 10**0.35},
        ),
        (
            "CS6_E_G2P_4_005",
            {-1.5: 10**-0.5, -2.0: 10**-0.3, -2.5: 10**-0.05, -3.0: 10**0.32},
        ),
        (
            "CS6_E_G2P_6_005",
            {-1.5: 10**-0.5, -2.0: 10**-0.3, -2.5: 10**-0.05, -3.0: 10**0.35},
        ),
        ("CS6_E_G2P_8_005", RmiddleOnes),
        ("CS6_E_G2P_10_005", RmiddleOnes),
        (
            "CS6_E_G2P_20_005",
            {-1.5: 10**-0.45, -2.0: 10**-0.25, -2.5: 10**-0.08, -3.0: 10**0.28},
        ),
        (
            "CS6_E_20_005",
            {-1.5: 10**-0.42, -2.0: 10**-0.23, -2.5: 1.0, -3.0: 10**0.3},
        ),
        ("DS1_E_G2P_0_000", RmiddleOnes),
        ("DS1_E_G2P_20_005", RmiddleOnes),
        ("DS1_E_20_005", {-1.5: 1.0, -2.0: 10**-0.18, -2.5: 1.0, -3.0: 1.0}),
        ("D2_E_G2P_0_000", RmiddleOnes),
        ("D2_E_G2P_20_005", RmiddleOnes),
        ("D2_E_20_005", RmiddleOnes),
        ("E_E_G2P_0_000", RmiddleOnes),
        ("E_E_G2P_20_005", RmiddleOnes),
        ("E_E_20_005", RmiddleOnes),
        ("Soft_B_E_G2P_0_000", {-1.5: 1, -2.0: 10**-0.3, -2.5: 1, -3.0: 1}),
        ("Soft_B_E_G2P_20_005", {-1.5: 1, -2.0: 10**0.2, -2.5: 1, -3.0: 1}),
        (
            "Soft_B_E_0_000",
            {-1.5: 10**-0.7, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        (
            "Soft_B_E_0_001",
            {-1.5: 10**-0.7, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        (
            "Soft_B_E_20_005",
            {-1.5: 10**-0.6, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 10**0.3},
        ),
        ("IIc_CS4_E_G2P_40_021", {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0}),
        ("CS5_E_G2P_30_005", {-1.5: 1.0, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 1.0}),
        ("IIc_CS5_E_G2P_40_021", {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0}),
        ("CS6_E_G2P_30_005", {-1.5: 1.0, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 1.0}),
        ("IIc_CS6_E_G2P_40_021", {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0}),
        ("DS1_E_G2P_40_021", {-1.5: 1.0, -2.0: 10**-0.35, -2.5: 1.0, -3.0: 1.0}),
        ("IIc_DS1_E_G2P_60_021", {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0}),
        ("Soft_D2_E_G2P_0_000", {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0}),
        ("Soft_D2_E_G2P_20_005", RmiddleOnes),
        ("Soft_D2_E_G2P_40_021", {-1.5: 1.0, -2.0: 10**-0.4, -2.5: 1.0, -3.0: 1.0}),
        (
            "IIc_Soft_D2_E_G2P_60_021",
            {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0},
        ),
        (
            "IId_Soft_D2_E_G2P_0_000",
            {-1.5: 1.0, -2.0: 10**-0.2, -2.5: 1.0, -3.0: 1.0},
        ),
        (
            "IId_Soft_D2_E_G2P_20_013",
            {-1.5: 1.0, -2.0: 10**-0.45, -2.5: 1.0, -3.0: 1.0},
        ),
        ("Soft_D2_E_20_005", {-1.5: 1.0, -2.0: 10**-0.18, -2.5: 1.0, -3.0: 1.0}),
    ]

Pos = SnapshotFile["PartType1/Coordinates"].value
Vel = SnapshotFile["PartType1/Velocities"].value
V = SnapshotFile["PartType1/Potential"].value
x = Pos[:, 0]
y = Pos[:, 1]
z = Pos[:, 2]
vx = Vel[:, 0]
vy = Vel[:, 1]
vz = Vel[:, 2]
minV = np.argmin(V)
xC = x[minV]
yC = y[minV]
zC = z[minV]
vxC = vx[minV]
vyC = vy[minV]
vzC = vz[minV]
R = modulus([x - xC, y - yC, z - zC])

if R_limit_10000:
    R_limit = 10000.0
    # F = F + "_R_limit_10000_DeltaG"
elif R_limit_5000:
    R_limit = 5000.0
    # F = F + "_R_limit_5000_DeltaG"
elif R_limit_50:
    R_limit = 50.0
    # F = F + "_R_limit_50_DeltaG"
elif R_limit_32:
    R_limit = 32.0
    # F = F + "_R_limit_32_DeltaG"
else:
    R_limit = 10.0
    # F = F + "_R_limit_10_DeltaG"

GoodIDs = np.where(R < R_limit)

if R_bin_automatic:
    R_limit_min = R_middle
    R_limit_max = R_middle
    a = 0
    x0 = x
    while len(x0) < 10000 or a == 0:
        R_limit_min -= 0.000005
        R_limit_max += 0.000005
        a += 1
        GoodIDs = np.where((R < R_limit_max) * (R > R_limit_min))
        x0 = x[GoodIDs[0]]

x = x[GoodIDs]
y = y[GoodIDs]
z = z[GoodIDs]
x -= np.median(x)
y -= np.median(y)
z -= np.median(z)
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs]
vx -= np.median(vx)
vy -= np.median(vy)
vz -= np.median(vz)
R_xyz = modulus([x, y, z])

if Fig_x_hist:
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.set_xlabel(r"$x-x_c$", fontsize=30)
    n, bins, patches = ax1.hist(x - xC, 500, normed=1, histtype="stepfilled")
    plt.setp(patches, "facecolor", "g", "alpha", 0.75)
    ax1.set_xlim(-40, 40)
    ax1.set_ylim(0.0, 0.4)

    ax2.set_xlabel(r"$y-y_c$", fontsize=30)
    n, bins, patches = ax2.hist(y - yC, 500, normed=1, histtype="stepfilled")
    plt.setp(patches, "facecolor", "g", "alpha", 0.75)
    ax2.set_title("Histograms of centralized positions", fontsize=30)
    ax2.set_xlim(-40, 40)
    ax2.set_ylim(0.0, 0.4)
    ax2.tick_params(
        axis="both",
        which="both",
        bottom="on",
        top="off",
        labelbottom="on",
        right="off",
        left="off",
        labelleft="off",
    )

    ax3.set_xlabel(r"$z-z_c$", fontsize=30)
    n, bins, patches = ax3.hist(z - zC, 500, normed=1, histtype="stepfilled")
    plt.setp(patches, "facecolor", "g", "alpha", 0.75)
    ax3.set_xlim(-40, 40)
    ax3.set_ylim(0.0, 0.4)
    # ax3.axes.get_yaxis().set_visible(False)
    ax3.tick_params(
        axis="both",
        which="both",
        bottom="on",
        top="off",
        labelbottom="on",
        right="off",
        left="off",
        labelleft="off",
    )
    # f.savefig(figure_path + "Fig_B_Final_x_hist_I.png")

if Fig_x_hist2d:
    f = plt.figure(figsize=(13, 11))
    plt.xlabel(r"$x-x_c$", fontsize=30)
    plt.ylabel(r"$y-y_c$", fontsize=30)
    plt.hexbin(x - xC, y - yC, gridsize=200)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.title(r"Histogram of centralized positions x and y (200 hexbins)", fontsize=30)
    # f.savefig(figure_path + "Fig_CS4_Final_x_hist2d_I.png")  # 'Fig_x_hist2d.png'

R_hob_par = R[GoodIDs]
# Declare number of particles
# if F.startswith(("Soft_B_", "E_")):
#     N = 10**6
# elif F.startswith(("CS4_", "CS5_", "CS6_", "DS1_", "Soft_D2_")):
#     N = 10**5
# elif F.startswith("CS1_"):
#     N = 10**4
# # Declare total mass
# if F.startswith("A_", "B_", "CS1_", "CS4_", "CS5_", "CS6_", "E_"):
#     M = 1.0
# elif F.startswith(("DS1_", "D2_", "Soft_D2_")):
#     M = 1.0 / 6.0
# # Define particle mass
# m = M / N

if Gamma == -2.0:
    r_2 = R_middle
    posR_par_in_halo = np.where(R_hob_par < r_2)
    nr_par_in_halo = len(posR_par_in_halo[0])
    # M_2 = nr_par_in_halo * m
    G = 1.0
    # v_circ_2 = (G * M_2 / r_2) ** 0.5

r = modulus([x, y, z])
v = modulus([vx, vy, vz])

if Fig_v_logr:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.plot(r, v, "bo", lw=3, ms=2)
    ax1.set_xlabel("r", fontsize=30)
    ax1.set_ylabel(r"velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$", fontsize=30)
    ax1.set_title(r"A IC (I: $\Delta G,R_{lim}=10^4$)", fontsize=30)
    ax2.plot(np.log10(r), v, "bo", lw=3, ms=2)
    ax2.set_xlabel(r"$\log r$", fontsize=30)
    ax2.yaxis.tick_right()
    # f.savefig(figure_path + "A_IC_v_logr.png")

if Fig_v_logr_r2:
    # r_r2 = r / r_2
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 11))
    f.subplots_adjust(hspace=0, wspace=0)
    # ax1.plot(r_r2, v, "bo", lw=3, ms=2)
    ax1.set_xlabel(r"$\frac{r}{r_{-2}}$", fontsize=30)
    ax1.set_ylabel(r"velocity, $v = \sqrt{v_x^2+v_y^2+v_z^2}$", fontsize=30)
    ax1.set_title(r"A 48_009 (I: $\Delta G,R_{lim}=10^4$)", fontsize=30)
    # ax2.plot(np.log10(r_r2), v, "bo", lw=3, ms=2)
    ax2.set_xlabel(r"$\log(\frac{r}{r_{-2}})$", fontsize=30)
    ax2.yaxis.tick_right()
    # f.savefig(figure_path + "A_48_009_v_logr_r2.png")

if Fig1_xy_xz:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 10))
    f.subplots_adjust(hspace=0, wspace=0)
    ax1.set_title(r"A IC ($R_{lim}=32$)", fontsize=30)
    ax1.set_xlabel("x", fontsize=30)
    ax1.set_ylabel("y", fontsize=30)
    ax1.plot(x, y, "bo", ms=2, mew=0)
    ax2.set_xlabel("x", fontsize=30)
    ax2.set_ylabel("z", fontsize=30)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    ax2.plot(x, z, "bo", ms=2, mew=0)
    # f.savefig(figure_path + "A_IC_xy_xz.png")

if Fig2_v:
    f = plt.figure()
    ax1 = plt.subplot(131)
    plt.ylabel("vx", fontsize=30)
    plt.plot(x, vx, "bo", ms=2, mew=0)
    ax2 = plt.subplot(132)
    plt.xlabel("x", fontsize=30)
    plt.ylabel("vy", fontsize=30)
    # plt.title("Velocities (File = %s)" % F, fontsize=30)
    plt.plot(x, vy, "bo", ms=2, mew=0)
    # setp(ax2.get_yticklabels(), visible=False)
    ax3 = plt.subplot(133)
    plt.ylabel("vz", fontsize=30)
    plt.plot(x, vz, "bo", ms=2, mew=0)
    # setp(ax3.get_yticklabels(), visible=False)
    # f.savefig(figure_path + 'A_v.png')

# v_r = vr_cartesian(x, y, z, vx, vy, vz)

min_binning_R = -1.5
max_binning_R = np.log10(R_limit)

if bins_202:
    nr_binning_bins = 202
    # F += "_200_radial_bins"
elif bins_102:
    nr_binning_bins = 102
    # F += "_100_radial_bins"
elif bins_52:
    nr_binning_bins = 52
    # F += "_50_radial_bins"
elif bins_22:
    nr_binning_bins = 22
    # F += "_20_radial_bins"
else:
    pass

# (
#     sigma2_arr,
#     sigmarad2_arr,
#     bin_radius_arr,
#     r_arr,
#     Phi_arr,
#     Theta_arr,
#     VR_arr,
#     VTheta_arr,
#     VPhi_arr,
#     VR_i_avg_arr,
# ) = bin_halo_radially()

# radii = bin_radius_arr
# sigma_r2 = sigmarad2_arr
# kappa_arr = kappa(sigma2_arr)

# len_obj_1 = density_arr
# len_obj = sigma2_arr
# density = density_arr
# gamma_arr = gamma(density_arr)

# sigmatheta2 = sigmatheta2_arr
# sigmarad2 = sigmarad2_arr
# beta_arr = beta()

# if Fig3_sigma:  # Dispersions
#     f = plt.figure(figsize=(16, 11))
#     x_plot = np.log10(bin_radius_arr)
#     y_plot = np.log10(sigma2_arr)
#     plt.plot(x_plot, y_plot, "r-o", ms=8, mew=0, label=r"$\log (\sigma_{total}^2)$")
#     y_plot = np.log10(sigmarad2_arr)
#     plt.plot(x_plot, y_plot, "b--s", ms=8, mew=0, label=r"$\log (\sigma_{r}^2)$")
#     y_plot = np.log10(sigmatheta2_arr)
#     plt.plot(x_plot, y_plot, "g--v", ms=8, mew=0, label=r"$\log (\sigma_{\theta}^2)$")
#     y_plot = np.log10(sigmaphi2_arr)
#     plt.plot(x_plot, y_plot, "k--^", ms=8, mew=0, label=r"$\log (\sigma_{\phi}^2)$")
#     y_plot = np.log10(sigmatan2_arr)  # plot sigma_tan
#     plt.plot(
#         x_plot,
#         y_plot,
#         "--^",
#         ms=8,
#         mew=0,
#         color="Violet",
#         label=r"$\log (\sigma_{tan}^2)$",
#     )
#     plt.xlabel(r"$\log $r", fontsize=30)
#     plt.ylabel(r"$\log(\sigma^2)$", fontsize=30)
#     # plt.title(r'Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)', fontsize=30)
#     leg = plt.legend(
#         prop=dict(size=30), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
#     )
#     leg.get_frame().set_alpha(0.5)
    # f.savefig(figure_path + 'B_sigma.png')

# if Fig3_sigma_r_2:  # Dispersions
#     f = plt.figure(figsize=(16, 11))
#     x_plot = np.log10(bin_radius_arr / r_2)
#     y_plot = np.log10(sigma2_arr)
#     plt.plot(x_plot, y_plot, "r-o", ms=8, mew=0, label=r"$\log (\sigma_{total}^2)$")
#     y_plot = np.log10(sigmarad2_arr)
#     plt.plot(x_plot, y_plot, "b--s", ms=8, mew=0, label=r"$\log (\sigma_{r}^2)$")
#     y_plot = np.log10(sigmatheta2_arr)
#     plt.plot(x_plot, y_plot, "g--v", ms=8, mew=0, label=r"$\log (\sigma_{\theta}^2)$")
#     y_plot = np.log10(sigmaphi2_arr)
#     plt.plot(x_plot, y_plot, "k--^", ms=8, mew=0, label=r"$\log (\sigma_{\phi}^2)$")
#     y_plot = np.log10(sigmatan2_arr)  # plot sigma_tan
#     plt.plot(
#         x_plot,
#         y_plot,
#         "--^",
#         ms=8,
#         mew=0,
#         color="Violet",
#         label=r"$\log (\sigma_{\tan}^2)$",
#     )
#     leg = plt.legend(
#         prop=dict(size=30), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
#     )
#     leg.get_frame().set_alpha(0.5)
#     plt.xlabel(r"$\log (\frac{r}{r_{-2}})$", fontsize=30)
#     plt.ylabel(r"$\log (\sigma^2)$", fontsize=30)
#     plt.title(
#         r"Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)", fontsize=30
#     )
#     f.savefig(figure_path + "B_IC_sigma_r_2.png")

# if Fig3_sigma_divided_by_v_circ_r_2:  # Dispersions
#     f = plt.figure(figsize=(16, 11))
#     x_plot = np.log10(bin_radius_arr / r_2)
#     y_plot = np.log10(sigma2_arr / v_circ_2**2)
#     # label=r'$\log ((\frac{\sigma_{total}}{v_{circ,2}})^2)$'
#     plt.plot(
#         x_plot, y_plot, "r-o", ms=8, mew=0, label=r"$\log (\bar{\sigma_{total}}^2)$"
#     )
#     y_plot = np.log10(sigmarad2_arr / v_circ_2**2)
#     plt.plot(x_plot, y_plot, "b--s", ms=8, mew=0, label=r"$\log (\bar{\sigma_{r}}^2)$")
#     y_plot = np.log10(sigmatheta2_arr / v_circ_2**2)
#     plt.plot(
#         x_plot, y_plot, "g--v", ms=8, mew=0, label=r"$\log (\bar{\sigma_{\theta}}^2)$"
#     )
#     y_plot = np.log10(sigmaphi2_arr / v_circ_2**2)
#     plt.plot(
#         x_plot, y_plot, "k--^", ms=8, mew=0, label=r"$\log (\bar{\sigma_{\phi}}^2)$"
#     )
#     y_plot = np.log10(sigmatan2_arr / v_circ_2**2)  # plot sigma_tan
#     plt.plot(
#         x_plot,
#         y_plot,
#         "--^",
#         ms=8,
#         mew=0,
#         color="Violet",
#         label=r"$\log (\bar{\sigma_{\tan}}^2)$",
#     )
#     plt.xlabel(r"$\log (\frac{r}{r_{-2}})$", fontsize=30)
#     # plt.ylabel(r'$\log (\frac{\sigma^2}{v_{circ,2}})$', fontsize=26)
#     plt.ylabel(r"$\log (\bar{\sigma}^2)$", fontsize=30)
#     plt.title(
#         r"Velocity dispersions (B IC, $R_{limit} = 10^4$, 20 radial bins)", fontsize=30
#     )
#     leg = plt.legend(
#         prop=dict(size=18), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
#     )
#     leg.get_frame().set_alpha(0.5)
#     f.savefig(figure_path + "B_sigma_divided_by_v_circ_r_2.png")

if Fig4_beta:  # plot beta
    f = plt.figure(figsize=(16, 11))
    # plt.xlim(-1., 1.0)
    plt.ylim(-1.0, 1.0)
    # x_plot = np.log10(bin_radius_arr)
    # y_plot = beta_arr
    plt.xlabel(r"$\log$r", fontsize=30)
    plt.ylabel(r"$\beta$", fontsize=30)
    # plt.plot(x_plot, y_plot, "k-o", ms=7, lw=2, mew=0)
    # plt.plot(x_plot, 0 * x_plot, "--", lw=2, color="grey")
    # plt.plot((-0.5, -0.5), (-1.0, 1.0), "r-", label="inner cut")
    # plt.plot((1., 1.), (-1., 1.), 'b-', label='outer cut')
    leg = plt.legend(
        prop=dict(size=30), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
    )
    leg.get_frame().set_alpha(0.5)
    # plt.title(r'$\beta$ with zero-line (B 199_093, $R_{limit}=32, 50$ bins)', fontsize=30)
    # f.savefig(figure_path + 'B_IC_beta_logr_I_R32.png')

if Fig4_beta_r_2:  # plot beta
    f = plt.figure(figsize=(16, 11))
    # plt.xlim(-1.7, 2.0)
    # plt.ylim(-.2, 1.)
    # x_plot = np.log10(bin_radius_arr / r_2)
    # y_plot = beta_arr
    plt.xlabel(r"$\log(\frac{r}{r_{-2}})$", fontsize=30)
    plt.ylabel(r"$\beta$", fontsize=30)

    # from this graph we see that beta is below zero.
    # this means sigmatheta2_arr/sigmarad2_arr > 1,
    # which in turn means that sigmatheta2_arr > sigmarad2_arr.
    # plt.plot(x_plot, y_plot, "k-o", ms=7, lw=2, mew=0, label=r"$\beta$")
     #plt.plot(x_plot, 0 * x_plot, "--", lw=2, color="grey")
    # plt.title(r'$\beta$ with zero-line(%s)' % F, fontsize=30)
    # plt.title('Velocity anisotropy (CS6 IC with 20 radial bins)', fontsize=30)
    # f.savefig(figure_path + 'B_IC_beta_r_2_logr.png')

if Fig5_kappa:
    f = plt.figure(figsize=(16, 11))
    # x_plot = np.log10(bin_radius_arr)
    # y_plot = kappa_arr
    plt.xlabel(r"$\log $r", fontsize=30)
    plt.ylabel(r"$\kappa$", fontsize=30)
    plt.ylim(-4.0, 0.4)
    # plt.plot(x_plot, y_plot, "k-o", ms=4, mew=0)
    plt.plot((-0.92, -0.92), (-5.0, 25.0), "r-", label="inner cut")
    leg = plt.legend(
        prop=dict(size=30), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
    )
    leg.get_frame().set_alpha(0.5)
    # plt.title(r'$\kappa$ and zero-line (B 199_093, $R_{limit}=32, 50$ bins)',fontsize=30)
    # f.savefig(figure_path + 'B_IC_kappa_logr_I_R32.png')

if Fig5_kappa_r_2:
    f = plt.figure(figsize=(16, 11))
    # x_plot = np.log10(bin_radius_arr / r_2)
    # y_plot = kappa_arr
    plt.xlabel(r"$\log (\frac{r}{r_{-2}})$", fontsize=30)
    plt.ylabel(r"$\kappa$", fontsize=30)
    # plt.plot(x_plot, y_plot, "k-o", ms=4, mew=0, label=r"$\kappa$")
    # plt.ylim(-2., .5)
    plt.title(r"$\kappa$ (B IC with 20 radial bins)", fontsize=30)
    # f.savefig(figure_path + "B_IC_kappa_r_2_logr.png")

if Fig6_gamma:
    f = plt.figure(figsize=(16, 11))
    # x_plot = np.log10(bin_radius_arr)
    # x_plot = np.log10(bin_radius_arr)
    plt.ylim(-4.0, 1.5)
    # y_plot = gamma_arr
    plt.xlabel(r"$\log $r", fontsize=30)
    plt.ylabel(r"$\gamma$", fontsize=30)
    # plt.plot(x_plot, y_plot, "k-o", ms=7, lw=2, mew=0)
    plt.plot((-0.5, -0.5), (-4.0, 4.0), "r-", label="inner cut")
    plt.plot((1.0, 1.0), (-4.0, 4.0), "b-", label="outer cut")
    leg = plt.legend(
        prop=dict(size=30), numpoints=2, ncol=1, fancybox=True, loc=0, handlelength=2.5
    )
    leg.get_frame().set_alpha(0.5)
    # plt.title('Radial density slope (B IC, $R_{limit}=32, 50$ bins)', fontsize=30)
    # f.savefig(figure_path + 'B_IC_gamma_logr_I_R32.png')

if Fig6_gamma_r_2:
    f = plt.figure(figsize=(16, 11))
    # x_plot = np.log10(bin_radius_arr / r_2)
    # y_plot = gamma_arr
    plt.xlabel(r"$\log (\frac{r}{r_{-2}})$", fontsize=30)
    plt.ylabel(r"$\gamma$", fontsize=30)
    # plt.plot(x_plot, y_plot, "k-o", ms=7, lw=2, mew=0, label=r"$\gamma$")
    # plt.title('Radial density slope (B IC with 20 radial bins)', fontsize=30)
    # f.savefig(figure_path + 'B_IC_gamma_r_2_logr.png')

if Fig7_betagamma:
    f = plt.figure()
    # subplot(121)
    plt.xlabel(r"$\beta$", fontsize=30)
    plt.ylabel(r"$\gamma$", fontsize=30)
    # plt.title(r"$\gamma$ vs $\beta$ (%s)" % F, fontsize=30)
    # plt.plot(beta_arr, gamma_arr, "k-o", ms=2, mew=0)
    # subplot(122)
    plt.xlabel(r"$\beta$", fontsize=30)
    plt.ylabel(r"$\kappa$", fontsize=30)
    plt.title(r"$\kappa$ vs $\beta$", fontsize=30)
    # plt.plot(beta_arr, kappa_arr, "k-o", ms=2, mew=0)
    # f.savefig(figure_path + 'B_betagamma.png')

# if save_lnr_beta_gamma_kappa_VR_r_sigma_r_rr2_rho:
    # logr_arr = np.array(np.log10(bin_radius_arr))
    # beta_arr = np.array(beta_arr)
    # gamma_arr = np.array(gamma_arr)
    # kappa_arr = np.array(kappa_arr)
    # r_arr = 10 ** (logr_arr)
    # sigmarad2_arr = np.array(sigmarad2_arr)
    # rho_arr = np.array(rho_arr)
    # GoodIDs = np.where(gamma_arr == gamma_arr)
    # logr_arr = logr_arr[GoodIDs]
    # gamma_arr = gamma_arr[GoodIDs]
    # beta_arr = beta_arr[GoodIDs]
    # kappa_arr = kappa_arr[GoodIDs]
    # r_arr = r_arr[GoodIDs]
    # sigmarad2_arr = sigmarad2_arr[GoodIDs]
    # VR_i_avg_in_bin_arr = VR_i_avg_in_bin_arr[GoodIDs]

    # if Gamma == -2.0:
        # r_r2_arr = r_arr / r_2
        # rho_arr = rho_arr[GoodIDs]
        # x = np.array(
        #     (
        #         logr_arr,
        #         beta_arr,
        #         gamma_arr,
        #         kappa_arr,
        #         VR_i_avg_in_bin_arr,
        #         r_arr,
        #         sigmarad2_arr,
        #         r_r2_arr,
        #         rho_arr,
        #     )
        # )
    #     x = x.transpose()
    #     out_name = text_files_path + F + ".txt"
    #     np.savetxt(
    #         out_name,
    #         x,
    #         delimiter=" ",
    #         header=" \t logr \t beta \t gamma \t kappa \t VR_avg \t r \t sigmarad2 \t r_r2 \t rho",
    #     )
    # else:
    #     x = np.array(
    #         (
    #             logr_arr,
    #             beta_arr,
    #             gamma_arr,
    #             kappa_arr,
    #             VR_i_avg_in_bin_arr,
    #             r_arr,
    #             sigmarad2_arr,
    #         )
    #     )
#         x = x.transpose()
#         out_name = text_files_path + F + ".txt"
#         np.savetxt(
#             out_name,
#             x,
#             delimiter=" ",
#             header=" \t logr \t beta \t gamma \t kappa \t VR_avg \t r \t sigmarad2",
#         )

# plt.show()

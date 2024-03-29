import h5py  # type: ignore

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore

from modulus import modulus  # type: ignore

# Filename = desktopPath / 'RunGadget/G_HQ_1000000_test\
#            /output/HQ10000_G0.8_2_000.hdf5'

snapshot_files = [
    "0G00_IC_000",
    "0G20_Final_000",
    "OMG00_001_IC_000",
    "OMG20_Final_000",
    "ics_10MPC_128_022",
    "ICS_10mpc_res256_022",
]

Filename = snapshot_files[0] + ".hdf5"
SnapshotFile = h5py.File(Filename, "r")

# radial and tangential velocities
v_t1_arr = []
v_t2_arr = []

# Initialize velocities
v_r = v_theta = v_phi = np.zeros([1000000, 1])
v_t = np.zeros([1000000, 3])
for i in range(1000000):
    v_r[i] = np.divide((Rvector[:, i] @ v_vector[:, i]), linalg.norm(Rvector[:, i]))

    v_t[i] = np.divide(
        np.cross(Rvector[:, i], v_vector[:, i], axis=0), linalg.norm(Rvector[:, i])
    )
    v_theta[i] = (vxnew[i] * ycl[i] - xcl[i] * vynew[i]) / (xcl[i] ** 2 + ycl[i] ** 2)
    v_phi[i] = (
        zcl[i] * (xcl[i] * vxnew[i] + ycl[i] * vynew[i])
        - (xcl[i] ** 2 + ycl[i] ** 2) * vznew[i]
    ) / ((xcl[i] ** 2 + ycl[i] ** 2 + zcl[i] ** 2) * modulus(xcl[i], ycl[i]))

plt.figure(1)
plt.xlabel(r"$v_r, v_{\theta}$ and $v_{\phi}$")
plt.ylabel("Number of particles")
plt.title(r"VDF of HQ structure with $10^6$ particles")
plt.hist(
    v_theta,
    bins=40,
    histtype="step",
    color="r",
    range=(-2, 2),
    label=r"$v_{\theta}$",
    lw=2,
)
plt.hist(
    v_phi, bins=40, histtype="step", color="b", range=(-2, 2), label=r"$v_{\phi}$", lw=2
)
plt.hist(v_r, bins=40, histtype="step", color="k", range=(-2, 2), label=r"$v_r$", lw=2)
plt.legend(
    prop=dict(size=13), numpoints=2, ncol=2, frameon=True, loc=2, handlelength=2.5
)
plt.show()

# Plot abs(v), then plot lin-log, log-lin, log-log.
# Plot at 3 different radial bins.
# Try to bin in log(v)
# And make a fit to exp(-v^2 / 2 s^2), to se the difference in the form

"""
v_ttrans = np.transpose(v_t)
print(f'{v_ttrans= }')

# Components of first direction vector for tangent plane
bx = np.ones(1000000)
by = -(vxnew * zcl - vznew * xcl) / (vznew * ycl - vynew * zcl)
bz = -(xcl + ycl * by) / (zcl)

# direction vectors for tangent plane
B1 = np.array([bx, by, bz])
print(f'{B1= }')

B2 = zeros([1000000, 3])
for i in range(1000000):
    B2[i] = np.cross(Rvector[:, i], B1[:, i]))
print(f'{B2= }')

# normalized direction vectors for tangent plane
t1 = t2 = zeros([1000000, 3])
B3 = np.transpose(B2)

for i in range(1000000):
    t1[i] = np.divide(B1[:, i], linalg.norm(B1[:, i]))
    t2[i] = np.divide(B3[:, i], linalg.norm(B3[:, i]))
print(f'{t1= }')
print(f'{t2= }')

# split v_t into two components
v_t1 = v_t2 = zeros([1000000, 1])

for i in range(1000000):
    v_t1[i] = (v_t[i, :] @ t1[i, :])
    v_t2[i] = (v_t[i, :] @ t2[i, :])
print(f'{v_t1 =}')
print(f'{v_t2 =}')
"""

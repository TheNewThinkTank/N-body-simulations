import h5py  # type: ignore
import numpy as np  # type: ignore

from Pathlib import Path  # type: ignore

path = Path.cwd()

old_snaps_list = [
    "G_HQ_1000000_B/output/Hernquist10000_G1.0_198_093",
    "G_HQ_1000000_B/output/Hernquist10000_G1.0_199_093",
    "G_OM_100000_C4/output/Osipkov_Merritt10000_G1.0_48_093",
    "G_OM_100000_C5/output/Osipkov_Merritt10000_G1.0_48_093",
    "G_OM_100000_C6/output/Osipkov_Merritt10000_G1.0_48_093",
    "G_OM_100000_D1/output/Osipkov_Merritt10000_G1.0_49_093",
    "G_Edd_100000_D2/output/Hernquist10000_G1.0_49_093",
]

old_snap_file = h5py.File(path + old_snaps_list[0] + ".hdf5", "r")

new_snaps_list = [
    "B_G1.0_198_093_no_free_par",
    "B_G1.0_199_093_rfp",
    "C4_G1.0_48_093_rfp",
    "C5_G1.0_48_093_rfp",
    "C6_G1.0_48_093_rfp",
    "D1_G1.0_49_093_rfp",
    "D2_G1.0_49_093_rfp",
]

new_snap_file = h5py.File(new_snaps_list[0] + ".hdf5", "w")

# copy header to new snapshot:
old_snap_file.copy("/Header", new_snap_file, "/Header")

masses = old_snap_file["PartType1/Masses"].value
Pos = old_snap_file["PartType1/Coordinates"].value
Vel = old_snap_file["PartType1/Velocities"].value
V = old_snap_file["PartType1/Potential"].value

x = Pos[:, 0]
y = Pos[:, 1]
z = Pos[:, 2]
vx = Vel[:, 0]
vy = Vel[:, 1]
vz = Vel[:, 2]
v = (vx**2 + vy**2 + vz**2) ** 0.5  # Speed
E_tot = V + 0.5 * v**2
GoodIDs = np.where(E_tot <= 0.0)  # Bound particles
x = x[GoodIDs]
y = y[GoodIDs]
z = z[GoodIDs]
vx = vx[GoodIDs]
vy = vy[GoodIDs]
vz = vz[GoodIDs]

# print(x.shape)
Pos = np.array([x, y, z])
Pos = Pos.transpose()
# print('Pos.shape: ', Pos.shape)
Vel = np.array([vx, vy, vz])
Vel = Vel.transpose()
# print('Vel.shape: ', Vel.shape)
# V = V[GoodIDs]  # Potential
# IPython.embed()
masses = masses[GoodIDs]

new_snap_file["PartType1/Masses"] = masses
new_snap_file["PartType1/Coordinates"] = Pos
new_snap_file["PartType1/Velocities"] = Vel
# NewSnapfile['PartType1/Potential'] = V

# Set Ndm:
Ndm = new_snap_file["PartType1/Coordinates"].shape[0]
# print('Ndm: ', Ndm)
# Ndm = NewSnapfile['PartType1/Masses'].shape[0]
Narray = np.array([0, Ndm, 0, 0, 0, 0], dtype=np.int32)
new_snap_file["Header"].attrs.modify("NumPart_ThisFile", Narray)
new_snap_file["Header"].attrs.modify("NumPart_Total", Narray)

new_snap_file.close()
old_snap_file.close()

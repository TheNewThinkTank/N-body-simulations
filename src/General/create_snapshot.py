import h5py  # type: ignore
import numpy as np  # type: ignore

old_snap_file = h5py.File("SNAPSHOT_FILENAME", "r")
new_snap_file = h5py.File("NEW_SNAPSHOT_FILENAME", "w")

# Copy header to new snapshot:
old_snap_file.copy("/Header", new_snap_file, "/Header")

# Set masses positions and velocities of new halos
new_snap_file["PartType1/Masses"] = old_snap_file["PartType1/Masses"].value  # Masses
new_snap_file["PartType1/Positions"] = old_snap_file["PartType1/Positions"].value  # Pos
new_snap_file["PartType1/Velocities"] = old_snap_file["PartType1/Velocities"].value  # Vel

# Set Ndm:
Ndm = new_snap_file["PartType1/Masses"].shape[0]
Narray = np.array([0, Ndm, 0, 0, 0, 0], dtype=np.int32)
new_snap_file["Header"].attrs.modify("NumPart_ThisFile", Narray)
new_snap_file["Header"].attrs.modify("NumPart_Total", Narray)

new_snap_file.close()
old_snap_file.close()

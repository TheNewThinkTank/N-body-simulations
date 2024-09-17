import os  # type: ignore
import subprocess  # type: ignore
import datetime  # type: ignore
from pathlib import Path  # type: ignore

line_count = "cat {} | wc -l"
PEP8_count = "pep8 {} | wc -l"

userPath = Path.cwd()
Logfile_ext = str(userPath).split("/")[-1]


def byte_to_str(byte_str):
    string = byte_str.decode("utf-8").lstrip().rstrip()
    return string


usr = "/Users/gustavcollinrasmussen/"
proj = "N-body-simulations/"
logpath = usr + proj + "StableStructures/docs/SystemLogs/"
logfile = logpath + f"KPI_{Logfile_ext}.txt"

kpi_list_sorted = []

with open(logfile, "a") as wf:
    wf.write("-" * 75 + "\n\n")
    wf.write(
        f"\n ********   Logging timestamp:\t{str(datetime.datetime.now())}"
        f"   ********\n\n\n"
    )
    KPI_list = []
    wf.write(
        "Module name \t\t\t Number of lines \t PEP-8 violations".rjust(50) + "\n\n"
    )
    file_count = 0
    total_line_count = 0
    total_pep8_count = 0
    # for root, dirs, files in os.walk("."):
    """
    root = "."
    for item in os.listdir(root):
        if ((not os.path.isfile(os.path.join(root, item))) or
            (item == ".DS_Store") or
            any(x in item for x in [".pyc", ".txt"])):
    """
    for item in os.listdir(userPath):
        if (
            (not os.path.isfile(os.path.join(userPath, item)))
            or any(x in item for x in [".pyc", ".txt", ".DS_Store"])
        ):
            continue
        else:
            filename = item
            lines = subprocess.check_output(line_count.format(filename), shell=True)
            PEP8 = subprocess.check_output(PEP8_count.format(filename), shell=True)
            KPI_list.append(
                {
                    "module": f"{filename}",
                    "lines": int(byte_to_str(lines)),
                    "PEP8_violations": int(byte_to_str(PEP8)),
                }
            )
            file_count += 1
            total_line_count += int(byte_to_str(lines))
            total_pep8_count += int(byte_to_str(PEP8))
        kpi_list_sorted = sorted(KPI_list, key=lambda KPI: KPI["lines"], reverse=True)
    for e in kpi_list_sorted:
        res_str = f"{e['module']:<40}{e['lines']:^4}{e['PEP8_violations']:>22}"
        wf.write(res_str + "\n")

    wf.write(
        f"\n\n{'*'*14}\tPython scripts:\t{file_count}\t{'*'*14}\n"
        f"\n\n{'*'*14}\tPEP8 violations:\t{total_pep8_count}\t{'*'*14}\n"
        f"\n\n{'*'*14}\tTotal code-lines:\t{total_line_count}\t{'*'*14}\n\n"
    )

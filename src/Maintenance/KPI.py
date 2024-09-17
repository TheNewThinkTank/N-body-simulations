import os
import subprocess
import datetime
from pathlib import Path

# Commands to count lines and PEP-8 violations in a file
line_count_cmd = "wc -l < {}"
pep8_count_cmd = "pycodestyle {} | wc -l"  # Use pycodestyle to count PEP-8 violations

# Path setup
project_path = Path.cwd()  # Current project directory
log_dir = project_path / "docs/system-logs"  # Log directory
logfile_name = f"kpi_{project_path.name}.txt"  # Log file name based on project folder
logfile = log_dir / logfile_name

# Create log directory if it doesn't exist
log_dir.mkdir(parents=True, exist_ok=True)

# Utility function to decode byte string and strip whitespaces
def byte_to_str(byte_str):
    return byte_str.decode("utf-8").strip()

# Function to generate project overview with PEP-8 violations
def generate_project_overview():
    # Initialize counters and data storage
    file_count = 0
    total_line_count = 0
    total_pep8_violations = 0
    kpi_list = []

    # Write log header
    with logfile.open("a") as wf:
        wf.write(f"{'-' * 75}\n\n")
        wf.write(f"{'*' * 8}\tLogging timestamp: {datetime.datetime.now()}\t{'*' * 8}\n\n\n")
        wf.write(f"{'Module name':<40}{'Lines':>10}{'PEP-8 Violations':>20}\n\n")

    # Iterate through Python files in the project directory
    for item in project_path.glob("**/*.py"):  # Recursively search for Python files
        if item.is_file():
            # Count lines in the file
            lines = subprocess.check_output(line_count_cmd.format(item), shell=True)
            line_count = int(byte_to_str(lines))

            # Count PEP-8 violations using pycodestyle
            pep8_violations = subprocess.check_output(pep8_count_cmd.format(item), shell=True)
            pep8_count = int(byte_to_str(pep8_violations))

            # Collect KPI data
            kpi_list.append({
                "module": str(item.relative_to(project_path)),
                "lines": line_count,
                "pep8_violations": pep8_count
            })

            # Update counters
            file_count += 1
            total_line_count += line_count
            total_pep8_violations += pep8_count

    # Sort files by line count in descending order
    kpi_list_sorted = sorted(kpi_list, key=lambda x: x["lines"], reverse=True)

    # Log data into the file
    with logfile.open("a") as wf:
        for kpi in kpi_list_sorted:
            wf.write(f"{kpi['module']:<40}{kpi['lines']:>10}{kpi['pep8_violations']:>20}\n")
        # Summary of the overview
        wf.write(f"\n\n{'*' * 14}\tPython scripts: {file_count}\t{'*' * 14}\n")
        wf.write(f"\n{'*' * 14}\tTotal code lines: {total_line_count}\t{'*' * 14}\n")
        wf.write(f"\n{'*' * 14}\tTotal PEP-8 violations: {total_pep8_violations}\t{'*' * 14}\n\n")


if __name__ == "__main__":
    generate_project_overview()

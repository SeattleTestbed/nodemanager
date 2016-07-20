"""
This setup script runs `nminit.py` to set up a vesselinfo file 
for the test nodemanager.
"""
# Ignore the status info that `nminit` prints while it runs
#pragma out
import subprocess
import nminit

nminit.initialize_state()


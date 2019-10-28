# DO NOT REMOVE THIS: FOLDER TREE WAS CREATED WRONG AND WILL WORK ONLY FROM ROOT

# subprocess

import subprocess  # permits to run other process from system

import os

# old school
# os.system('calc')

PAYLOADS_PATH = os.path.join(".", "payloads")
FEATURE_X_PATH = os.path.join(PAYLOADS_PATH, "feature_y")
FEATURE_Y_PATH = os.path.join(PAYLOADS_PATH, "feature_y")

complete_p = subprocess.run(['payload.bat'],
                            shell=True,
                            cwd=FEATURE_X_PATH,
                            capture_output=True,
                            env={"user": "gradu",
                                 "dut": "raspberry",
                                 "cwd": FEATURE_X_PATH}
                            )
print(complete_p.returncode)
print(complete_p.stdout)
print(complete_p.stderr)


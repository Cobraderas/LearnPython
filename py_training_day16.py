# DO NOT REMOVE THIS: FOLDER TREE WAS CREATED WRONG AND WILL WORK ONLY FROM ROOT

# subprocess

import subprocess  # permits to run other process from system

import os

# old school
# os.system('calc')

PAYLOADS_PATH = os.path.join(".", "payloads")
FEATURE_X_PATH = os.path.join(PAYLOADS_PATH, "feature_x")
FEATURE_Y_PATH = os.path.join(PAYLOADS_PATH, "feature_y")

# complete_p = subprocess.run(
#                             ['payload.bat'],
#                             shell=True,
#                             cwd=FEATURE_X_PATH,
#                             capture_output=True,
#                             env={"user": "gradu",
#                                  "dut": "raspberry",
#                                  "cwd": FEATURE_X_PATH}
#                             )


# complete_p = subprocess.run(
#                             ['payload.bat'],
#                             shell=True,
#                             cwd=FEATURE_Y_PATH,
#                             capture_output=True,
#                             env={"test_path": "c:\\"}
#                             )
# print(complete_p.returncode)
# print(complete_p.stdout)
# xxx = str(complete_p.stdout, encoding="UTF-8").splitlines()
# for line in xxx:
#     print(line)
# print(complete_p.stderr)

# subprocess.run("calc")

import shlex
# our_command = "dir c:\\windows"
# our_command = r"explorer c:\\"
#
# args = shlex.split(our_command)
# # subprocess.run(args, shell=True)
# subprocess.run(args, shell=False)
# print(args)


mpopen = subprocess.Popen(["payload.bat"],
                          shell=True,
                          cwd=FEATURE_X_PATH,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          env={
                              "user": "gradu",
                              "dut": "raspberry",
                              "cwd": FEATURE_X_PATH}
                          )
print(mpopen.poll())
print(mpopen.communicate())
print(mpopen.poll())
print(mpopen.wait(1))


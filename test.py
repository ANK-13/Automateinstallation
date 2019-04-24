import subprocess

try:
   out = subprocess.check_output("date", shell=True).decode("utf-8")
   print(type(out))  
   print(out)                   
except subprocess.CalledProcessError as grepexc:                                                                                                   
    print("error code", grepexc.returncode, grepexc.output)
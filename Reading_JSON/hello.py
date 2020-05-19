#! /usr/bin/python
import subprocess;
import os;

s1= "Welcome"
print(s1)

def run_cmd(args_list):
        print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err

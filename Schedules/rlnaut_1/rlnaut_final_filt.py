#!/usr/bin/env python

import sys
import subprocess
import os


##-----------------------------------------------------------------------------------#
errormsg = ""
class Arg(object):
    _registry = []
    def __init__(self, flag, value, req):
        self._registry.append(self)
        self.flag = flag
        self.value = value
        self.req = req

def make_arg(flag, value, req):
    Argument = Arg(flag, value, req)
    if Argument.req == True:
        if Argument.flag not in sys.argv:
            print(errormsg)
            sys.exit("ERROR: required argument '{0}' is missing".format(Argument.flag))
    if Argument.value == True:
        try:
            test = sys.argv[sys.argv.index(Argument.flag)+1]
        except ValueError:
            if Argument.req == True:
                print(errormsg)
                sys.exit("ERROR: required argument '{0}' is missing".format(Argument.flag))
            elif Argument.req == False:
                return False
        except IndexError:
                print(errormsg)
                sys.exit("ERROR: argument '{0}' requires a value".format(Argument.flag))
        else:
            if Argument.value == True:
                Argument.value = sys.argv[sys.argv.index(Argument.flag)+1]
        
    if Argument.value == False:
        if Argument.flag in sys.argv:
            Argument.value = True
        else:
            Argument.value = False
    return Argument.value
##-----------------------------------------------------------------------------------#
try:
	print("++ Matt's rlnaut final filter ++")
	outdir = make_arg('--o',True,True)
	inmodel = make_arg('--in_3dref',True,True)
	mail = make_arg('--mail',True,True)
	subprocess.call('relion_image_handler --i {0} --o {1}/rlnaut_initial_model.mrc --lowpass 15'.format(inmodel,outdir),shell=True)
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_SUCCESS'.format(outdir)])
	if mail == 'True':
		cwd = os.getcwd()
		mailout = open('mail.txt','w')
		mailout.write('''rlnaut running in {0} has finished!'''.format(cwd))
		mailout.close()
		subprocess.call('mail -s "Relion Automated Finished" `whoami`@leeds.ac.uk < mail.txt',shell=True)
except:
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_FAILURE'.format(outdir)])	

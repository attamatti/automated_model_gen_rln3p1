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
		mailout.write('''rlnaut running in {0} has finished!\n\n'''.format(cwd))
		classdata = open('External/job007/run.out','r').readlines()
		writeit = False
		for i in classdata:
			if 'Minimized particle set contains' in i:
				writeit = True
			if writeit == True:
				mailout.write(i)

		imdata = open('InitialModel/job008/run_it300_model.star','r').readlines()
		n=0
		for i in imdata:
			if 'data_model_classes' in i:
				reso = imdata[n+10].split()[5]
				FC = imdata[n+10].split()[6]
			n+=1
	
		mailout.write('''\nUNFILTERED MODEL RESOLUTION: {0} \nOVERALL FOURIER COMPLETENESS: {1}\n'''.format(reso,FC))
		if float(reso) < 15:
			mailout.write('Final model filtered to 15 A')
		mailout.close()
		subprocess.call('Schedules/rlnaut_1/rlnaut_make_image.py',shell=True)
		subprocess.call('mail -s "Relion Automated Finished" -a final_classes.png `whoami`@leeds.ac.uk < mail.txt',shell=True)
except:
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_FAILURE'.format(outdir)])	

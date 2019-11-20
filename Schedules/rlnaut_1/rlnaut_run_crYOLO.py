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
	print("++ Matt's rlnaut run crYOLO ++")
	outdir = make_arg('--o',True,True)
	model = make_arg('--model',True,True)
	boxsize = make_arg('--boxsize',True,True)
	rawname = make_arg('--rawname',True,True)
	indir = '/'.join(make_arg('--in_mics',True,True).split('/')[0:-1])
	indir = '{0}/{1}'.format(indir,rawname)
	FNULL = open(os.devnull, 'w')
## make config file
	configout = open('config.json','w')
	configout.write('''{{
    "model" : {{
        "architecture":         "PhosaurusNet",
        "input_size":           1024,
        "anchors":              [{0},{0}],
        "max_box_per_image":    150,
        "num_patches":          1,
        "filter":               [0.1,"filtered"]
    }}
}}
'''.format(boxsize))
	configout.close()
	print('Successfully made config.json')
	print('Ran {}'.format(' '.join(['cryolo_predict.py','-c','config.json','-w',model,'-i','{0}/'.format(indir),'-g','0,1','-o',outdir,'-t','0.3'])))

	subprocess.call(['/absl/EM/emsoftware2/env-modules/install/crYOLO/1.3.5/bin/cryolo_predict.py','-c','config.json','-w',model,'-i','{0}/'.format(indir),'-g','0,1','-o',outdir,'-t','0.3'],stderr=FNULL)
	subprocess.call(['touch','{0}/coords_suffix.star'.format(outdir)])
	subprocess.call(['mv','{0}/STAR'.format(outdir),'{0}/{1}'.format(outdir,indir.split('/')[-1])])
	print('Output is: {0}coords_suffix.star'.format(outdir))
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_SUCCESS'.format(outdir)])
except:
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_FAILURE'.format(outdir)])	

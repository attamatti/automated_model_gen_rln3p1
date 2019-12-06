#!/usr/bin/env python3

####################################################################
##               may need to update these paths                   ##
####################################################################
default_cryolo_model='/absl/SCRATCH/Users/fbsmi/rln_auto/schedule/Schedules/rlnaut_1/gmodel_phosnet_201909.h5'
rlnaut_zipfile= '/fbs/emsoftware2/LINUX/fbsmi/scripts/workshop/rln_automated/rlnaut_v2.tar.gz'
####################################################################

import subprocess
import sys
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





## get the user input:
errormsg='''
Required arguments:
--apix		<number>	Angstrom/pixel
--boxsize	<number>	Estimated box size to be used for refinement	
--raw_data	<directory>	The name of the directory where the raw data are


Optional arguments:
--cryolo_model  <modelfile.h5>  Custom trained crYOLO model to use
                                otherwise will use the default: 
                                gmodel_phosnet_201909.h5'''

print('''
:::::::::::::::::::::::::::::::::::::
::         rlnaut v1 setup         ::
:::::::::::::::::::::::::::::::::::::
''')
pxsize = make_arg('--apix',True,True)
boxsize = make_arg('--boxsize',True,True)
raw_data = make_arg('--raw_data',True,True)
yolomodel = make_arg('--cryolo_model',True,False)
nozip = make_arg('--nozip',False,False)

if yolomodel == False:
	print(':: Using default crYOLO model ::')
	yolomodel = default_cryolo_model
elif os.path.isfile(yolomodel) == False:
	yolomodel = default_cryolo_model
	print(":: Can't find specified crYOLO model ::\nusing {0}".format(yolomodel))
else:
	print(':: Using custom crYOLO model::\n{0}'.format(yolomodel))

if nozip == True:
	print(':: Unpacking ::')
	subprocess.call('tar -zxvf {0}'.format(rlnaut_zipfile),shell=True)

print(':: Writing jobfiles ::')
print('using crYOLO model: {0}'.format(yolomodel))
### update the files
print('Schedules/rlnaut_1/Import/job.star')
output = open('Schedules/rlnaut_1/Import/job.star','w')
output.write('''
# version 30001

data_job

_rlnJobType                             0
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
        Cs        2.7 
        Q0        0.1 
    angpix         {0} 
beamtilt_x          0 
beamtilt_y          0 
  do_other         No 
  do_queue         No 
    do_raw        Yes 
fn_in_other    ref.mrc 
 fn_in_raw {1}/*.mrc 
    fn_mtf         "" 
is_multiframe        Yes 
        kV        300 
min_dedicated          1 
 node_type "Particle coordinates (*.box, *_pick.star)" 
optics_group_name opticsGroup1 
optics_group_particles         "" 
other_args         "" 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
'''.format(pxsize,raw_data))
output.close()

print('Schedules/rlnaut_1/crYOLO/job.star')
output = open('Schedules/rlnaut_1/crYOLO/job.star','w')
output.write('''
# version 30001

data_job

_rlnJobType                            99
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
  do_queue         No 
    fn_exe Schedules/rlnaut_1/rlnaut_run_crYOLO.py 
  in_3dref         "" 
 in_coords         "" 
   in_mask         "" 
    in_mic MotionCorr/job002/corrected_micrographs.star 
    in_mov         "" 
   in_part         "" 
min_dedicated          1 
nr_threads          1 
other_args         "" 
param10_label         "" 
param10_value         "" 
param1_label    boxsize 
param1_value         {0} 
param2_label    rawname 
param2_value         {1} 
param3_label      model 
param3_value         {2} 
param4_label         "" 
param4_value         "" 
param5_label         "" 
param5_value         "" 
param6_label         "" 
param6_value         "" 
param7_label         "" 
param7_value         "" 
param8_label         "" 
param8_value         "" 
param9_label         "" 
param9_value         "" 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
'''.format(boxsize,raw_data,yolomodel))
output.close()

print('Schedules/rlnaut_1/Extract/job.star')
output = open('Schedules/rlnaut_1/Extract/job.star','w')
output.write('''
# version 30001

data_job

_rlnJobType                             5
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
    angpix          1 
bg_diameter         -1 
black_dust          5 
coords_suffix External/job004/coords_suffix.star 
do_cut_into_segments        Yes 
do_extract_helical_tubes        Yes 
do_extract_helix         No 
 do_invert        Yes 
   do_norm        Yes 
  do_queue         No 
do_recenter         No 
do_reextract         No 
do_rescale        Yes 
do_reset_offsets         No 
do_set_angpix         No 
extract_size        {0} 
fndata_reextract         "" 
helical_bimodal_angular_priors        Yes 
helical_nr_asu          1 
helical_rise          1 
helical_tube_outer_diameter        200 
min_dedicated          1 
    nr_mpi         16 
other_args         "" 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
recenter_x          0 
recenter_y          0 
recenter_z          0 
   rescale        128 
 star_mics CtfFind/job003/micrographs_ctf.star 
white_dust          5 '''.format(boxsize))
output.close()

print('Schedules/rlnaut_1/Class2D/job.star')
output = open('Schedules/rlnaut_1/Class2D/job.star','w')
output.write('''
# version 30001

data_job

_rlnJobType                             8
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
ctf_intact_first_peak         No 
do_bimodal_psi        Yes 
do_combine_thru_disc         No 
do_ctf_correction        Yes 
do_fast_subsets         No 
  do_helix         No 
do_parallel_discio        Yes 
do_preread_images        Yes 
  do_queue         No 
do_restrict_xoff        Yes 
do_zero_mask        Yes 
dont_skip_align        Yes 
   fn_cont         "" 
    fn_img Extract/job005/particles.star 
   gpu_ids        0:1 
helical_rise       4.75 
helical_tube_outer_diameter        200 
highres_limit         -1 
min_dedicated          1 
nr_classes         50 
   nr_iter         25 
    nr_mpi          6 
   nr_pool          3 
nr_threads          4 
offset_range          5 
offset_step          1 
other_args         "" 
particle_diameter        {0} 
psi_sampling          6 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
 range_psi          6 
scratch_dir         "" 
 tau_fudge          2 
   use_gpu        Yes 
'''.format(int(0.8*float(boxsize))))
output.close()


print('Schedules/rlnaut_1/InitalModel/job.star')
output = open('Schedules/rlnaut_1/InitalModel/job.star','w')
output.write('''
# version 30001

data_job

_rlnJobType                            18
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
ctf_intact_first_peak         No 
do_combine_thru_disc         No 
do_ctf_correction        Yes 
   do_pad1         No 
do_parallel_discio        Yes 
do_preread_images         No 
  do_queue         No 
do_solvent        Yes 
   fn_cont         "" 
    fn_img External/job007/minimal_classes.star 
   gpu_ids        0:1 
min_dedicated          1 
nr_classes          1 
    nr_mpi          6 
   nr_pool          3 
nr_threads          5 
offset_range          6 
offset_step          2 
other_args         "" 
particle_diameter        {0} 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
  sampling "15 degrees" 
scratch_dir         "" 
sgd_fin_iter         50 
sgd_fin_resol         15 
sgd_fin_subset_size        500 
sgd_inbetween_iter        200 
sgd_ini_iter         50 
sgd_ini_resol         35 
sgd_ini_subset_size        100 
sgd_sigma2fudge_halflife         -1 
sgd_write_iter         10 
skip_gridding         No 
  sym_name         C1 
   use_gpu        Yes 
'''.format(int(0.8*float(boxsize))))
output.close()
print(':: Done! ::')

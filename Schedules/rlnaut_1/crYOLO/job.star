
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
param1_value        300 
param2_label    rawname 
param2_value   Raw_data 
param3_label      model 
param3_value Schedules/rlnaut_1/gmodel_phosnet_201909.h5 
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
 

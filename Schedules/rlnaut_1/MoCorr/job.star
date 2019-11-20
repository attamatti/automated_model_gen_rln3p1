
# version 30001

data_job

_rlnJobType                             1
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
   bfactor        150 
bin_factor          1 
do_dose_weighting        Yes 
do_own_motioncor         No 
  do_queue         No 
dose_per_frame          1 
first_frame_sum          1 
 fn_defect         "" 
fn_gain_ref         "" 
fn_motioncor2_exe /fbs/emsoftware2/LINUX/MotionCor2/MotionCor2_1.1.0-Cuda80 
 gain_flip "No flipping (0)" 
  gain_rot "No rotation (0)" 
   gpu_ids        0:1 
group_for_ps          4 
group_frames          1 
input_star_mics Import/job001/movies.star 
last_frame_sum         -1 
min_dedicated          1 
    nr_mpi          2 
nr_threads          1 
other_args         "" 
other_motioncor2_args         "" 
   patch_x          1 
   patch_y          1 
pre_exposure          0 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
 save_noDW         No 
   save_ps         No 
 

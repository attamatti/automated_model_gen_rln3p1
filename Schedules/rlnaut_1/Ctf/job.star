
# version 30001

data_job

_rlnJobType                             2
_rlnJobIsContinue                       0
 

# version 30001

data_joboptions_values

loop_ 
_rlnJobOptionVariable #1 
_rlnJobOptionValue #2 
       box        512 
   ctf_win         -1 
      dast        100 
     dfmax      50000 
     dfmin       5000 
    dfstep        500 
    do_EPA         No 
do_ignore_ctffind_params        Yes 
do_phaseshift         No 
  do_queue         No 
fn_ctffind_exe ""/fbs/emsoftware2/LINUX/fbsmi/ctffind4/ctffind --omp-num-threads 1 --old-school-input"" 
fn_gctf_exe /fbs/emsoftware2/LINUX/fbssdr/Gctf/Gctf-v1.18_sm_30_cu8.0_x86_64 
   gpu_ids        0:1 
input_star_mics MotionCorr/job002/corrected_micrographs.star 
min_dedicated          1 
    nr_mpi          2 
other_args         "" 
other_gctf_args         "" 
 phase_max        180 
 phase_min          0 
phase_step         10 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
    resmax          5 
    resmin         30 
slow_search         No 
use_ctffind4         No 
  use_gctf        Yes 
use_given_ps         No 
  use_noDW         No 
 

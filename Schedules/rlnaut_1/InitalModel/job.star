
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
particle_diameter        280 
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
 

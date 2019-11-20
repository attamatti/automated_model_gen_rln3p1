
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
particle_diameter        280 
psi_sampling          6 
      qsub       qsub 
qsubscript /public/EM/RELION/relion/bin/relion_qsub.csh 
 queuename    openmpi 
 range_psi          6 
scratch_dir         "" 
 tau_fudge          2 
   use_gpu        Yes 
 


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
extract_size        300 
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
white_dust          5 
 

#########################################
LEEDS USAGE ONLY PLEASE! - many paths are still hardcoded
#########################################

quickly generates an up to 15A starting model from 1st 50 or so micrographs
  
1) Copy ~50 raw micrograph movies into the Raw_data directoty 

2) source rlnaut.bashrc

3) run setup_rlnaut.py

	Required arguments:
	--apix		<number>	Angstrom/pixel
	--boxsize	<number>	Estimated box size to be used for refinement	
	--raw_data	<directory>	The name of the directory where the raw data are

	Optional arguments:
	--cryolo_model  <modelfile.h5>  Custom trained crYOLO model to use
        	                        otherwise will use the default: 
        	                        gmodel_phosnet_201909.h5

4) run relion and select Schedules -> rlnaut_1

5) press run

6) It should finish in ~ 30 min

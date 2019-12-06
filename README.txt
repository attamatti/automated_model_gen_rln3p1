Quickly generates an up to 15A starting model from 1st 50 or so micrographs with no human intervention. 
Run the setup script and press go! 
Evaluate a dataset on-the-fly! 
Get an inital model before the full dataset has even finished collecting! 
FUN! FUN! FUN! 

It has so far worked for everything I've tested it on.  If you use this schedule please get back to me about the results (positive or negative).

What the Schedule does:

1) MotionCorr - through relion

2) gCTF - through relion

3) Picks particles - with crYOLO 

4) 2D classification

5) Class selection and angle equalization

6) Model generation with relion's SGD

7) Final filtering

All this is implemented through relion with a few of my scripts.  

Class selection in very crude at the moment; it takes all classes with greated than 1.9% of the particles.  This will be replaced with more robust class selection (using Cinderella) in later versions. 

Angle equalization makes it so the most populated class only has 2x as many particles as the least populated class.  This gives much improved results if there is a preferred orientation in the data.

Final filtering is to 15 A.

The script assumes 2 GPUs called 0 and 1. None of the steps have been full optimized for speed, so it can probably be made even faster.
If you are unhappy with any of the parameters in the various jobs they can be edited through the Relion interface.

##############################################################
EXTERNAL USERS
##############################################################
1) Copy the Schedules directory into the working directoty

2) Make a directory for your raw data and put ~50 microhraph movies in it


3) Make sure you have working copies of relion 3.1 and crYOLO installed

4) Change the path to cryolo on line 73 of Schedules/rlnaut_1/rlnaur_run_crYOLO.py to your copy of crYOLO

5) Run the setup script:
	./setup_rlnaut_v2.py --apix <pixelsize in A> --boxsize <boxsize in px> --raw_data <name of raw data dir> --cryolo_model <full path to crYOLO model> --nozip

6) run relion and select Schedules -> rlnaut_1

7) press run

8) It should finish in ~ 30 min

##############################################################
FULL VERSION FOR LEEDS USAGE - many paths are still hardcoded
##############################################################

quickly generates an up to 15A starting model from 1st 50 or so micrographs
  
1) Copy ~50 raw micrograph movies into the Raw_data directoty 

2) source rlnaut.bashrc

3) run setup_rlnaut.py

	Required arguments:
	--apix		<number>	Angstrom/pixel
	--boxsize	<number>	Estimated box size to be used for refinement	
	--raw_data	<directory>	The name of the directory where the raw data are

	Optional arguments:
	--cryolo_model  <modelfile.h5>  Full path to Custom trained crYOLO 
					model to use otherwise will use the 
					default: gmodel_phosnet_201909.h5

4) run relion and select Schedules -> rlnaut_1

5) press run

6) It should finish in ~ 30 min

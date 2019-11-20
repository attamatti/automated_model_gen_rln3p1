
# version 30001

data_pipeline_general

_rlnPipeLineJobCounter                      10
 

# version 30001

data_pipeline_processes

loop_ 
_rlnPipeLineProcessName #1 
_rlnPipeLineProcessAlias #2 
_rlnPipeLineProcessType #3 
_rlnPipeLineProcessStatus #4 
Schedules/rlnaut_1/Import/       None            0            1 
Schedules/rlnaut_1/MoCorr/       None            1            1 
Schedules/rlnaut_1/Ctf/       None            2            1 
Schedules/rlnaut_1/crYOLO/       None           99            1 
Schedules/rlnaut_1/Extract/       None            5            1 
Schedules/rlnaut_1/Class2D/       None            8            1 
Schedules/rlnaut_1/AngNorm/       None           99            1 
Schedules/rlnaut_1/InitalModel/       None           18            1 
Schedules/rlnaut_1/final_filt/       None           99            1 
 

# version 30001

data_pipeline_nodes

loop_ 
_rlnPipeLineNodeName #1 
_rlnPipeLineNodeType #2 
Schedules/rlnaut_1/Import/movies.star            0 
Import/job001/movies.star            0 
Schedules/rlnaut_1/MoCorr/corrected_micrographs.star            1 
Schedules/rlnaut_1/MoCorr/logfile.pdf           13 
MotionCorr/job002/corrected_micrographs.star            1 
Schedules/rlnaut_1/Ctf/micrographs_ctf.star            1 
Schedules/rlnaut_1/Ctf/logfile.pdf           13 
CtfFind/job003/micrographs_ctf.star            1 
External/job004/coords_suffix.star            2 
Schedules/rlnaut_1/Extract/particles.star            3 
Extract/job005/particles.star            3 
Schedules/rlnaut_1/Class2D/run_it025_data.star            3 
Schedules/rlnaut_1/Class2D/run_it025_model.star            8 
Class2D/job006/run_it025_data.star            3 
External/job007/minimal_classes.star            3 
Schedules/rlnaut_1/InitalModel/run_it300_data.star            3 
Schedules/rlnaut_1/InitalModel/run_it300_model.star            8 
Schedules/rlnaut_1/InitalModel/run_it300_class001.mrc            6 
InitialModel/job008/run_it300_class001.mrc            6 
 

# version 30001

data_pipeline_input_edges

loop_ 
_rlnPipeLineEdgeFromNode #1 
_rlnPipeLineEdgeProcess #2 
Import/job001/movies.star Schedules/rlnaut_1/MoCorr/ 
MotionCorr/job002/corrected_micrographs.star Schedules/rlnaut_1/Ctf/ 
MotionCorr/job002/corrected_micrographs.star Schedules/rlnaut_1/crYOLO/ 
CtfFind/job003/micrographs_ctf.star Schedules/rlnaut_1/Extract/ 
External/job004/coords_suffix.star Schedules/rlnaut_1/Extract/ 
Extract/job005/particles.star Schedules/rlnaut_1/Class2D/ 
Class2D/job006/run_it025_data.star Schedules/rlnaut_1/AngNorm/ 
External/job007/minimal_classes.star Schedules/rlnaut_1/InitalModel/ 
InitialModel/job008/run_it300_class001.mrc Schedules/rlnaut_1/final_filt/ 
 

# version 30001

data_pipeline_output_edges

loop_ 
_rlnPipeLineEdgeProcess #1 
_rlnPipeLineEdgeToNode #2 
Schedules/rlnaut_1/Import/ Schedules/rlnaut_1/Import/movies.star 
Schedules/rlnaut_1/MoCorr/ Schedules/rlnaut_1/MoCorr/corrected_micrographs.star 
Schedules/rlnaut_1/MoCorr/ Schedules/rlnaut_1/MoCorr/logfile.pdf 
Schedules/rlnaut_1/Ctf/ Schedules/rlnaut_1/Ctf/micrographs_ctf.star 
Schedules/rlnaut_1/Ctf/ Schedules/rlnaut_1/Ctf/logfile.pdf 
Schedules/rlnaut_1/Extract/ Schedules/rlnaut_1/Extract/particles.star 
Schedules/rlnaut_1/Class2D/ Schedules/rlnaut_1/Class2D/run_it025_data.star 
Schedules/rlnaut_1/Class2D/ Schedules/rlnaut_1/Class2D/run_it025_model.star 
Schedules/rlnaut_1/InitalModel/ Schedules/rlnaut_1/InitalModel/run_it300_data.star 
Schedules/rlnaut_1/InitalModel/ Schedules/rlnaut_1/InitalModel/run_it300_model.star 
Schedules/rlnaut_1/InitalModel/ Schedules/rlnaut_1/InitalModel/run_it300_class001.mrc 
 

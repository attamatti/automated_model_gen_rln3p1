
# version 30001

data_schedule_general

_rlnScheduleName                       Schedules/rlnaut_1/
_rlnScheduleCurrentNodeName            Import
 

# version 30001

data_schedule_jobs

loop_ 
_rlnScheduleJobNameOriginal #1 
_rlnScheduleJobName #2 
_rlnScheduleJobMode #3 
_rlnScheduleJobHasStarted #4 
   AngNorm    AngNorm        new            0 
   Class2D    Class2D        new            0 
       Ctf        Ctf        new            0 
   Extract    Extract        new            0 
    Import     Import        new            0 
InitalModel InitalModel        new            0 
    MoCorr     MoCorr        new            0 
    crYOLO     crYOLO        new            0 
final_filt final_filt        new            0 
 

# version 30001

data_schedule_edges

loop_ 
_rlnScheduleEdgeInputNodeName #1 
_rlnScheduleEdgeOutputNodeName #2 
_rlnScheduleEdgeIsFork #3 
_rlnScheduleEdgeOutputNodeNameIfTrue #4 
_rlnScheduleEdgeBooleanVariable #5 
    Import     MoCorr            0  undefined  undefined 
    MoCorr        Ctf            0  undefined  undefined 
       Ctf     crYOLO            0  undefined  undefined 
    crYOLO    Extract            0  undefined  undefined 
   Extract    Class2D            0  undefined  undefined 
   Class2D    AngNorm            0  undefined  undefined 
   AngNorm InitalModel            0  undefined  undefined 
InitalModel final_filt            0  undefined  undefined 
 

export PATH=/fbs/emsoftware2/LINUX/fbsmi/relion3.1/relion/build/bin:$PATH
export LD_LIBRARY_PATH=/fbs/emsoftware2/LINUX/fbsmi/relion3.1/relion/external/fftw/lib:/fbs/emsoftware2/LINUX/fbsmi/relion3.1/relion/external/fltk/lib:/fbs/emsoftware2/LINUX/fbsmi/relion3.1/relion/build/lib:$LD_LIBRARY_PATH

export RELION_GCTF_EXECUTABLE="/fbs/emsoftware2/LINUX/fbssdr/Gctf/Gctf-v1.18_sm_30_cu8.0_x86_64"
export RELION_MOTIONCOR2_EXECUTABLE="/fbs/emsoftware2/LINUX/MotionCor2/MotionCor2_1.1.0-Cuda80"
export RELION_RESMAP_EXECUTABLE="/fbs/emscratch2/bmbnar/relion/ResMap-1.1.4-linux64"
export RELION_CTFFIND_EXECUTABLE='"/fbs/emsoftware2/LINUX/fbsmi/ctffind4/ctffind  --omp-num-threads 1 --old-school-input"'
export RELION_PDFVIEWER_EXECUTABLE='evince'
export RELION_UNBLUR_EXECUTABLE='/fbs/emsoftware2/LINUX/fbsmi/unblur_1.0.2/bin/unblur_openmp_7_17_15.exe'
export RELION_SUMMOVIE_EXECUTABLE='/fbs/emsoftware2/LINUX/fbsmi/summovie_1.0.2/bin/sum_movie_openmp_7_17_15.exe'
module load crYOLO/1.3.5

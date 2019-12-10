#!/usr/bin/env python

import sys
import subprocess



#-----------------------------------------------------------------------------------#
errormsg = ""
class Arg(object):
    _registry = []
    def __init__(self, flag, value, req):
        self._registry.append(self)
        self.flag = flag
        self.value = value
        self.req = req

def make_arg(flag, value, req):
    Argument = Arg(flag, value, req)
    if Argument.req == True:
        if Argument.flag not in sys.argv:
            print(errormsg)
            sys.exit("ERROR: required argument '{0}' is missing".format(Argument.flag))
    if Argument.value == True:
        try:
            test = sys.argv[sys.argv.index(Argument.flag)+1]
        except ValueError:
            if Argument.req == True:
                print(errormsg)
                sys.exit("ERROR: required argument '{0}' is missing".format(Argument.flag))
            elif Argument.req == False:
                return False
        except IndexError:
                print(errormsg)
                sys.exit("ERROR: argument '{0}' requires a value".format(Argument.flag))
        else:
            if Argument.value == True:
                Argument.value = sys.argv[sys.argv.index(Argument.flag)+1]
        
    if Argument.value == False:
        if Argument.flag in sys.argv:
            Argument.value = True
        else:
            Argument.value = False
    return Argument.value
#-----------------------------------------------------------------------------------#


def read_3p1star(infile):
	inDMCloop = False
	labels,data = {},[]
	dta = open(infile,'r').readlines()[0:100]
	for i in dta:
		if i.split()== ['data_model_classes']:
			inDMCloop = True
		elif i.strip('\n') == '# version 30001':
			inDMCloop = False
		if inDMCloop == True:
			if '_rln' in i:
				labels[i.split()[0]] = int(i.split()[1].replace('#',''))-1
			elif len(i.split()) == len(labels) and len(i.split()) > 0:		
				data.append(i.split())
	return(labels,data)
				

def get_classes(data,labels,param,value):
	valdic = {}
	
	for i in data:
		try:
			valdic[float(i[labels[param]])].append(i)
		except:
			valdic[float(i[labels[param]])] = [i]	
	if value == 'max':
		return(valdic[max(valdic)])
	if value == 'min':
		return(valdic[min(valdic)])
	else:
		hits = []
		for i in valdic:
			if i > value:
				for j in valdic[i]:
					hits.append(j)
		return(hits)

def read_parts_file(partsfile):
	n=0
	pd = open(partsfile,'r').readlines()
	labels,header,data = {},[],[]
	indata = False
	inplabs = False
	for i in pd:	
		if indata == False:
			header.append(i)
			if i.split() == ['data_particles']:
				inplabs = True
			if inplabs == True and '_rln' in i:
				labels[i.split()[0]] = int(i.split()[1].replace('#',''))-1	
			if '_rln' in i and '_rln' not in pd[n+1] and inplabs == True:
				indata = True			
		elif indata == True and len(i.split()) == len(labels) and len(i.split()) != 0:
			data.append(i.split())
		n+=1
	return(labels,header,data)
try:
	print("++ Matt's rlnaut minimal class select ++\n")
	outdir = make_arg('--o',True,True)
	inparts = make_arg('--in_parts',True,True)
	thresh = float(make_arg('--thresh',True,True))
	inmodel = inparts.replace('_data','_model')
	print('particle count threshold: {0}'.format(thresh))
	labels,data = read_3p1star(inmodel) 
	returnclass = get_classes(data,labels,'_rlnClassDistribution',0.019)
	goodclasses = []
	for i in returnclass:
		goodclasses.append(int(i[labels['_rlnReferenceImage']].split('@')[0]))
	goodclasses.sort()
	print('Selected {0} classes: {1}'.format(len(goodclasses),goodclasses))
	plabels,pheader,pdata = read_parts_file(inparts)
	output = open('{0}/selected_particles.star'.format(outdir),'w')
	for i in pheader:
		output.write(i)
	theclasses = {}
	partcount = 0
	for i in pdata:
		if int(i[plabels['_rlnClassNumber']]) in goodclasses:
			output.write('{}\n'.format('  '.join(i)))
			try:
				theclasses[int(i[plabels['_rlnClassNumber']])].append(i)
				partcount +=1
			except:
				theclasses[int(i[plabels['_rlnClassNumber']])] = [i]
				partcount+=1
	
	## count the particles in each class 
	minno = min([len(theclasses[x]) for x in theclasses])
	for i in theclasses:
		theclasses[i].sort(key=lambda x: x[plabels['_rlnMaxValueProbDistribution']],reverse=True)
	
	minout = open('{0}/minimal_classes.star'.format(outdir),'w')
	
	## make the minimal output starfile
	for i in pheader:
		minout.write(i)
	classcount = {}
	minpcount = 0
	for i in theclasses:
		if len(theclasses[i]) >= 2*minno:
			for j in theclasses[i][:(2*minno)]:
				minout.write('{}\n'.format(' '.join(j)))
			classcount[i] = 2*minno
			minpcount+=2*minno
		else:
			for j in theclasses[i]:
				minout.write('{}\n'.format(' '.join(j)))
			classcount[i] = len(theclasses[i])
			minpcount+=len(theclasses)
	
	if 2*minpcount < 500:
		im_jobfile = open('Schedules/rlnaut_1/InitalModel/job.star','r')
		lines = im_jobfile.readlines()
		lines[42] = 'sgd_fin_subset_size        {0}'.format(2*minno)
		im_jobfile.close()
		im_jobfile = open('Schedules/rlnaut_1/InitalModel/job.star','w')
		im_jobfile.writelines(lines)
		im_jobfile.close()
		print('less than 500 particles in final set!\n using sgd_fin_subset_size of {0}'.format(2*minno))
	
	print('\n+ Minimized set stats +\nclass\tparts\tweight')
	for i in goodclasses:
		print('{0}\t{1}\t{2:0.2f}'.format(i,classcount[i],float(classcount[i])/(minno*2)))
	print('\nMinimized particle set contains {0} particles'.format(minpcount))
	print('Minimized set written to: {0}'.format('{0}/minimal_classes.star\n'.format(outdir)))
	print('Full particle set contains {0} particles'.format(partcount))
	print('Full set written to: {0}'.format('{0}/selected_particles.star'.format(outdir)))
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_SUCCESS'.format(outdir)])
except:
	subprocess.call(['touch','{0}/RELION_JOB_EXIT_FAILURE'.format(outdir)])	

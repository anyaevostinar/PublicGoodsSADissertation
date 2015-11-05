#######
# A script to make an event file for Avida based on a resource file. It sets resource amounts of random cells based on the resource amount that was produced in the experimental run. This is to create control runs that have the same resources but not the behavior that produces the resource.
#####
from random import randint

resource_file = '/data/resource.dat'
world_size = 40000
##The resource that you want injected into the control world
in_res = 'cellulase'

#treatments =['lyse_long_10k','lyse_long_00002','lyse_long_002', 'lyse_long_02', 'lyse_long_01']
#treatments = ['lyse_long_1k']
#treatments = ['lyse_long_4k']
treatments = ['lyse_long_40k']
reps = range(51,80)

event_file = 'config/events'
header = 'u begin InjectRange lyse-not.org 0 '+str(world_size-1)+"\nu 0:100:end PrintAverageData \nu 0:100:end PrintDominantData \nu 0:100:end PrintCountData \nu 0:100:end PrintTasksData \nu 0:100:end PrintTimeData \nu 0:100:end PrintKaboom \nu 0:100:end PrintInstructionData \nu 0:100:end PrintQuorum \nu 0:1:end PrintResourceData resource.dat 0 \n"

### You need to indicate what column the desired resource is here, 1-indexed
col = 5


for t in treatments:
    for r in reps:
        resources = open(t+"_"+str(r)+resource_file, 'r')
        event = open(event_file+"_"+t+"_"+str(r)+".cfg", 'w')
        event.write(header)
        for line in resources:
            if len(line)>1 and line[0] != '#':
                split = line.split()
                update = split[0]
                res_amount = int(split[col-1])
                injections = res_amount/10
                for i in range(injections):
                    event.write('u '+update+' InjectCellResource '+str(randint(0, world_size-1))+" "+in_res+" 10\n")
        event.write("\nu 0:10000:end SavePopulation \nu 100000 Exit\n")
        resources.close()
        event.close()

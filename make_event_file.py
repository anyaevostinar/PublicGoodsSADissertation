#######
# A script to make an event file for Avida based on a resource file. It sets resource amounts of random cells based on the resource amount that was produced in the experimental run. This is to create control runs that have the same resources but not the behavior that produces the resource.
#####
from random import randint

resource_file = '/data/resource.dat'
world_size = 10000
##The resource that you want injected into the control world
in_res = 'cellulase'

treatments =['lyse_long_10k']
reps = range(51,80)

event_file = 'config/events'
header = 'u begin InjectRange lyse-not.org 0 '+str(world_size-1)+"\n u 0:100:end PrintAverageData \n u 0:100:end PrintDominantData \n u 0:100:end PrintCountData \n u 0:100:end PrintTasksData \n u 0:100:end PrintTimeData \n u 0:100:end PrintKaboom \n u 0:100:end PrintInstructionData \n u 0:100:end PrintQuorum \n u 0:1:end PrintResourceData resource.dat 0 \n"

### You need to indicate what column the desired resource is here, 1-indexed
col = 5


for t in treatments:
    for r in reps:
        resources = open(t+"_"+str(r)+resource_file, 'r')
        event = open(event_file+"_"+t+"_"+str(r)+".cfg", 'w')
        event.write(header)
        for line in resources:
            if line and line[0] != '#':
                split = line.split()
                res_amount = split[col-1]
                update = split[0]
                event.write('u '+update+' SetCellResource '+str(randint(0, world_size-1))+" "+in_res+" "+res_amount+"\n")
        event.write("\n u 0:10000:end SavePopulation \n u 100000 Exit\n")
        resources.close()
        event.close()

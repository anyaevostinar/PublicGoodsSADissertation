fun_list = open('run_list_4k', 'w')
header = 'set description longterm \nset email vostinar@msu.edu \nset email_when final \nset config_dir /mnt/home/anyaejo/PublicGoods/LongTerm/config \nset dest_dir /mnt/home/anyaejo/PublicGoods/LongTerm \nset class_pref 95 \nset walltime 4 \nset mem_request 3\n\n\n'
fun_list.write(header)

reps = range(51,81)
#treatments = ['lyse_long_1k', 'lyse_long_4k', 'lyse_long_10k', 'lyse_long_00002', 'lyse_long_002', 'lyse_long_02', 'lyse_long_01']

treatments = ['lyse_long_4k']

#settings_1 = ['./avida -s $seed -set COPY_MUT_PROB .0002 -set WORLD_X 25 -set WORLD_Y 40 -set EVENT_FILE events', './avida -s $seed -set COPY_MUT_PROB .0002 -set WORLD_X 50 -set WORLD_Y 80 -set EVENT_FILE events', './avida -s $seed -set COPY_MUT_PROB .0002 -set WORLD_X 100 -set WORLD_Y 100 -set EVENT_FILE events', './avida -s $seed -set COPY_MUT_PROB .00002 -set WORLD_X 100 -set WORLD_Y 100 -set EVENT_FILE events', './avida -s $seed -set COPY_MUT_PROB .002 -set WORLD_X 100 -set WORLD_Y 100 -set EVENT_FILE events','./avida -s $seed -set COPY_MUT_PROB .02 -set WORLD_X 100 -set WORLD_Y 100 -set EVENT_FILE events','./avida -s $seed -set COPY_MUT_PROB .01 -set WORLD_X 100 -set WORLD_Y 100 -set EVENT_FILE events']

settings_1 = ['./avida -s $seed -set COPY_MUT_PROB .0002 -set WORLD_X 50 -set WORLD_Y 80 -set EVENT_FILE events']

settings_2 = ' -def INST_SET instset-heads.cfg -set ENVIRONMENT_FILE environment-control.cfg -set KABOOM_PROB .05 -set NO_MUT_INSTS "A"\n\n'


for t in range(len(treatments)):
    for r in reps:
        line = str(r)+" "+treatments[t]+"_cont "+settings_1[t]+"_"+treatments[t]+"_"+str(r)+".cfg"+settings_2
        fun_list.write(line)

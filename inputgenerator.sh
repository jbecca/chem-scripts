#!/bin/sh

#script to make input files and folders for DIM/QM calculations based off of a template file

for i in $(seq 01 1 100)
    do
    if [ "$i" -le "9" ]; then
        ii=0$i
        python ~/Programs/scripts/copytemplate.py -c pyr_water_ag_${i}_geom.run -t template.run -o $ii-geom.run
    else
        ii=$i
        python ~/Programs/scripts/copytemplate.py -c pyr_water_ag_${i}.run -t template.run -o $ii-geom.run
    fi
    echo $ii
#    mkdir ./$ii
    #First make all of the files
    #echo pyr_water_ag_${ii}_geom.run
    #python ~/Programs/scripts/copytemplate.py -c pyr_water_ag_${i}_geom.run -t template.run -o $ii-geom.run
    #wrap to copytemplate.py script to put correct QM coords in file
    #Move files to correct folders
    done
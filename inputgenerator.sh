#!/bin/sh

#script to make input files and folders for DIM/QM calculations based off of a template file

for i in $(seq 01 1 99)
    do
    if [ "$i" -le "9" ]; then
        ii=0$i
    else
        ii=$i
    fi
    echo $ii
    mkdir ./$ii
    #First make all of the files
    #wrap to copytemplate.py script to put correct QM coords in file
    #Move files to correct folders
    done
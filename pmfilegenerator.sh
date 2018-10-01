#!/bin/bash
# Hard coded script for now for making many frames of numerical differentiated 
# raman calculation files from the same template
for i in $(ls *-freq.out)
    do
    framenum=${i%-freq.out}
    mkdir $framenum
    python ~/Programs/scripts/nmodes2numdiff.py -t template.run $i
    mkdir $framenum/runfiles
    mv $i $framenum
    mv mode**.run $framenum/runfiles
    done

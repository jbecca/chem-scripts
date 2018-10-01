#!/bin/sh

#script to make input files and folders for DIM/QM calculations based off of a template file

for i in $(ls *.out)
    do
        ii=${i%-geom.out}
        python ~/Programs/scripts/copytemplate.py -c $i -t template.run -o $ii-freq.run
        echo $ii
    done
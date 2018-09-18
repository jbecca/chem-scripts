#!/bin/bash
# This script uses sed to remove a specific amount of DIM dipoles from the system
# In this case, it removes the water atoms and dipoles from a DIM output file
# based on hard coded line numbers from the order of the DIM system

for i in $(ls *.out)
    do 
    output=${i%.out}-rmwat.out
    echo $output
    sed -n '1, 88 p' $i > $output #input block
    sed -n '45089, 50846p' $i >> $output #coordinates wanted
    sed -n '140847, 152330p' $i >> $output #induced dipoles in X
    sed -n '242331, 253814p' $i >> $output #induced dipoles in Y
    sed -n '343815, 355345p' $i >> $output #induced dipoles in Z to end of file
    done
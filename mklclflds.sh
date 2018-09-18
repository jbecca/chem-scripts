#!/bin/bash

#script to make local field files from DIM output files
# in this case, done for shg calculations, so we need two different
# dim calculations. since shg is (w,w;2w), the lower frequency
# will be done first and copied to a file twice, then the higher freq.

# for now, this is pretty hard coded using sed and line numbers. 
a='50847, 152322p'
b='152331, 253806p'
c='253815, 355290p'
a2='140847, 152322p'
b2='242331, 253806p'
c2='343815, 355290p'
for i in $(ls ??-05659.out)
    do
    output=lclflds-${i%-05659.out}.txt
    output2=lclflds-${i%-05659.out}-rmwat.txt
    j=${i%05659.out}11318.out
    echo $output
    echo $i
    echo $j
    file1=fld1.out
    echo '             X' > $file1
    sed -n "${a}" $i >> $file1
    echo '             Y' >> $file1
    sed -n "${b}" $i >> $file1
    echo '             Z' >> $file1
    sed -n "${c}" $i >> $file1
    sed -i 's/(R)//g' $file1
    sed -i 's/(I)//g' $file1
    file2=fld2.out
    echo '             X' > $file2
    sed -n "${a}" $j >> $file2
    echo '             Y' >> $file2
    sed -n "${b}" $j >> $file2
    echo '             Z' >> $file2
    sed -n "${c}" $j >> $file2
    sed -i 's/(R)//g' $file2
    sed -i 's/(I)//g' $file2
    cut -c 14-90 $file1 > $file1.cut
    cut -c 14-90 $file2 > $file2.cut

    value='0.05659'
    value2='0.11318'

    echo "$value $value $value2" > $output
    echo "1" >> $output
    cat $file1.cut >> $output
    echo "2" >> $output
    cat $file1.cut >> $output
    echo "3" >> $output
    cat $file2.cut >> $output


    file1=fld1.out
    echo '             X' > $file1
    sed -n "${a2}" $i >> $file1
    echo '             Y' >> $file1
    sed -n "${b2}" $i >> $file1
    echo '             Z' >> $file1
    sed -n "${c2}" $i >> $file1
    sed -i 's/(R)//g' $file1
    sed -i 's/(I)//g' $file1
    file2=fld2.out
    echo '             X' > $file2
    sed -n "${a2}" $j >> $file2
    echo '             Y' >> $file2
    sed -n "${b2}" $j >> $file2
    echo '             Z' >> $file2
    sed -n "${c2}" $j >> $file2
    sed -i 's/(R)//g' $file2
    sed -i 's/(I)//g' $file2
    cut -c 14-90 $file1 > $file1.cut
    cut -c 14-90 $file2 > $file2.cut

    value='0.05659'
    value2='0.11318'

    echo "$value $value $value2" > $output2
    echo "1" >> $output2    
    cat $file1.cut >> $output2
    echo "2" >> $output2
    cat $file1.cut >> $output2
    echo "3" >> $output2
    cat $file2.cut >> $output2
    rm fld1.out*
    rm fld2.out*
    done

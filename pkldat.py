from chem import collect
import cPickle as pickle
import sys

fname = sys.argv[1]
print('collecting ' + str(fname))
f = collect(str(fname))
print('collecting raman derivatives')
f.collect_raman_derivatives()
print('dumping raman pickle')
pickle.dump( f, open("raman.pickle", "wb"))

print('collecting ' + str(fname))
f = collect(str(fname))
print('collecting hyper-raman derivatives')
f.collect_raman_derivatives(hpol=True)
print('dumping hyper-raman pickle')
pickle.dump( f, open("hraman.pickle", "wb"))



#tuples
#sets
#dictionary
TF_mot={'a':'ggg', 's':'cccc', 'd':'aaa'}
print TF_mot

TF_mot['q']='ttt'
print TF_mot

del TF_mot['a']
print TF_mot

TF_mot.update({'s':'caca'})
print TF_mot

print list(TF_mot.keys())

print list(TF_mot.values())
import os
print os.path.abspath('C:\\Python27\\practises\\')
print os.path.dirname(os.path.abspath("C:\\Python27\\practises\\")),'path'

print os.path.dirname(os.path.dirname(os.path.abspath('C:\\Python27\practises\\'))),'--'
print os.path.split(os.path.dirname(os.path.abspath('C:\\Python27\\practises\\')))[0],'=='

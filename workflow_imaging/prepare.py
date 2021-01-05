from workflow_imaging.pipeline import subject, imaging
import numpy as np
from os import getenv

# -------------- Insert new "Subject" --------------
print('Inserting Subject')

subjects = [{'subject': getenv('EXAMPLE_SUBJECT_NAME', 'subjectname'), 'sex': 'F', 'subject_birth_date': '2020-05-06 15:20:01'}]

subject.Subject.insert(subjects, skip_duplicates=True)

# -------------- Insert new "ProcessingParamSet" for Suite2p --------------
print('Inserting ProcessingParamSet for Suite2p')

params = np.load('./params/suite2p_default.npy', allow_pickle=True).item()

imaging.ProcessingParamSet.insert_new_params(
    'suite2p', 0, 'Calcium imaging analysis with Suite2p using default Suite2p parameters', params)

# -------------- Insert new "ProcessingParamSet" for CaImAn --------------
print('Inserting ProcessingParamSet for CaIman')

params = np.load('./params/caiman_2d_default.npy', allow_pickle=True).item()

imaging.ProcessingParamSet.insert_new_params(
    'caiman', 1, 'Calcium imaging analysis with CaImAn using default CaImAn parameters for 2d planar images', params)

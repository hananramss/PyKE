# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'FC_diagnosis_rules.krb'):
           [1713282164.6736717, 'FC_diagnosis_rules_fc.py'],
         ('', '', 'questions.kqb'):
           [1713282164.702056, 'questions.qbc'],
         ('', '', 'symptoms.kfb'):
           [1713282164.7109911, 'symptoms.fbc'],
        },
        compiler_version)


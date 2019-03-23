import json
import numpy as np
import glob, re


json_files = glob.glob('SSSP/*.json')
for fi in json_files:
    with open(fi, 'r') as fh:
        pp = json.load(fh)
    rgrid = np.array(pp['pseudo_potential']['radial_grid'])
    npoints = pp['pseudo_potential']['header']['mesh_size']

    if npoints != rgrid.shape[0]:
        print('mismatch in ', fi)
        print('mesh size: ', npoints)
        print('rgrid.shape: ', rgrid.shape)
        pp['pseudo_potential']['header']['mesh_size'] = int(rgrid.shape[0])

        with open(fi, 'w') as fout:
            # Match comma, space, newline and an arbitrary number of spaces ',\s\n\s*' with the
            # following conditions: a digit before (?<=[0-9]) and a minus or a digit after (?=[-|0-9]).
            # Replace found sequence with comma and space.
            fout.write(re.sub(r"(?<=[0-9]),\s\n\s*(?=[-|0-9])", r", ", json.dumps(pp, indent=2)))

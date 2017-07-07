"""
Defines the Simulation class for setting up containing information on a
metadynamics simulation.

Copyright (C) 2017 Thomas John Heavey IV

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

theavey@bu.edu
thomasjheavey@gmail.com
"""


# I will attempt to be python 2/3 compatible, but no guarantees.
# I'm planning on writing in python 3 primarily, but some dependencies may
# not be python 3 compatible.
from __future__ import print_function


class Simulation(object):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.cvs = None
        self.restraints = None
        self.molecules = None
        self.run_parameters = None
        self.metad_parameters = None
        self.Universe = None
        self.mdp_name = None
        self.tpr_name = None
        self.plumed_name = None
        self.minim_out_basename = None
        self.equil_out_basename = None
        self.hills_name = None
        self.colvar_name = None
        try:
            resume_name = kwargs['resume']
            self.set_from_resume(resume_name)
        except KeyError:
            # Though this method would look neater: https://stackoverflow.com/a/18677839/3961920
            pass

    def set_from_resume(self, resume_name):
        """
        Setup object by resuming old instance from a file

        :param resume_name:
        :return:
        """
        # TODO write this
        raise NotImplementedError

    def add_molecule(self, geom_name, name='mol', **kwargs):
        """
        Add a molecule to the simulation.

        :param geom_name:
        :param name:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def add_molectule_params(self, param_names):
        """
        Add parameter files for a molecule already added to the simulation.

        :param param_names:
        :return:
        """
        raise NotImplementedError

    def combine_molecules(self):
        """"""
        raise NotImplementedError

    def add_solvent(self, geom_name, params_name, box_side=3.0):
        """
        Add solvent (solvate) all molecules already added.

        :param geom_name:
        :param params_name:
        :param box_side: The size for the side of the box, assuming a cubic box (in nm)
        :return:
        """
        raise NotImplementedError

    def add_cv(self):
        """
        Define a collective variable for either metadynamics or restraint.

        :return:
        """
        raise NotImplementedError

    def add_restraint(self, cv, value, kappa):
        """
        Restrain simulation along given CV with given parameters

        :param cv:
        :param value:
        :param kappa:
        :return:
        """
        raise NotImplementedError

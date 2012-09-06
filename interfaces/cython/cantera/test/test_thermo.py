import unittest
import numpy as np

import cantera as ct
from . import utilities

class TestThermoPhase(utilities.CanteraTest):
    def setUp(self):
        self.phase = ct.Solution('h2o2.xml')

    def test_nSpecies(self):
        self.assertEqual(self.phase.nSpecies, 9)

    def test_setComposition(self):
        X = np.zeros(self.phase.nSpecies)
        X[2] = 1.0
        self.phase.setMoleFractions(X)
        Y = self.phase.massFractions

        self.assertEqual(list(X), list(Y))

    def test_badLength(self):
        X = np.zeros(5)
        with self.assertRaises(ValueError):
            self.phase.setMoleFractions(X)

    def test_getState(self):
        self.assertNear(self.phase.pressure, ct.OneAtm)
        self.assertNear(self.phase.temperature, 300)
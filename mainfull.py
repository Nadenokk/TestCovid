import unittest
from download_rez_DT_vector import DownloadDTVector
from otchet_for_epidemiologists import OtchetForEpidemiologists
from passengers_violators import PassengersViolators
from pulkovo import CreatePulcovo
from positiv_VICH import Vich2
# Get all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(Vich2)
tc2 = unittest.TestLoader().loadTestsFromTestCase(DownloadDTVector)
tc3 = unittest.TestLoader().loadTestsFromTestCase(OtchetForEpidemiologists)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PassengersViolators)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CreatePulcovo)
# Create a test suite combining
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
smokeTest._cleanup = False
unittest.TextTestRunner(verbosity=2).run(smokeTest)

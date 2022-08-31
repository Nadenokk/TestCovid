import unittest
from create_OKI3 import CreateOKI3
from download_rez_DT_vector import DownloadDTVector
from new_tablet import NewTablet
from otchet_for_epidemiologists import OtchetForEpidemiologists
from passengers_violators import PassengersViolators
from pulkovo import CreatePulcovo
from positiv_VICH import Vich2
# Get all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(Vich2)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NewTablet)
tc3 = unittest.TestLoader().loadTestsFromTestCase(DownloadDTVector)
tc4 = unittest.TestLoader().loadTestsFromTestCase(OtchetForEpidemiologists)
tc5 = unittest.TestLoader().loadTestsFromTestCase(PassengersViolators)
tc6 = unittest.TestLoader().loadTestsFromTestCase(CreatePulcovo)
tc7 = unittest.TestLoader().loadTestsFromTestCase(CreateOKI3)
# Create a test suite combining
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7])
smokeTest._cleanup = False
unittest.TextTestRunner(verbosity=2).run(smokeTest)

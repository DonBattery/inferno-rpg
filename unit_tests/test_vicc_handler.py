import unittest

import sys
import os

# Hozzáadjuk az app könyvtárat (ami a test könyvtárral egy "szinten" van) a PATH-hoz.
# ez kell ahhoz, hogy a teszt esetén is jól működjenek az importok.
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
print("APP IMPORT PATH", app_path)
sys.path.append(app_path)

from app.handlers import handle_vicc

class TestHandleHelp(unittest.TestCase):

    def test_handle_vicc(self):
        vicc_text = handle_vicc()
        assert "Ígyszól az egyik:" in vicc_text
        assert "Mire a másik:" in vicc_text

if __name__ == '__main__':
    unittest.main()
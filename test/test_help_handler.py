import unittest

import sys
import os

# Hozzáadjuk az app könyvtárat (ami a test könyvtárral egy "szinten" van) a PATH-hoz.
# ez kell ahhoz, hogy a teszt esetén is jól működjenek az importok.
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
print("APP IMPORT PATH", app_path)
sys.path.append(app_path)

from app.handlers import handle_help

class TestHandleHelp(unittest.TestCase):

    def test_single_argument(self):
        help_text = handle_help({}, "sajt")
        assert "A `!sajt` nem ismert parancs." in help_text

    def test_multiple_arguments(self):
        help_text = handle_help({}, "help", "vicc")
        assert "A !help paranccsal információt kaphatsz a játékban használható parancsokról." in help_text
        assert not "A !vicc parancs generál egy új viccet" in help_text

    def test_no_arguments(self):
        help_text = handle_help({})
        assert "Használható parancsok:" in help_text

if __name__ == '__main__':
    unittest.main()
from example_lab import __version__
from example_lab.example_lab import tasneem


def test_version():
    assert __version__ == '0.1.0'

def test_tasneem():
    expected = 11
    actual = tasneem(5,7)    
    assert actual == expected


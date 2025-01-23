import pytest
from main import dodaj, odejmij

def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0
    assert dodaj(0, 0) == 0

def test_odejmij():
    assert odejmij(5, 3) == 2
    assert odejmij(0, 5) == -5
    assert odejmij(10, 10) == 0

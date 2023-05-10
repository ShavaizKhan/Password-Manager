from project import load_key
from project import add
from project import view

def test_load_key():
    assert load_key() == b'lxlMo4Ey7lAixa6BeyHEchAecEzfWyMBt4UlesCjb10='

def test_add():
    assert add("Shavaiz", "Khan") == None

def test_view():
    assert view() == None
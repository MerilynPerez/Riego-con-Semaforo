from src.controller import Controller

def test_controller_thresholds():
    c = Controller()
    assert c.decide(0.10).action == 'ON'
    assert c.decide(0.40).action is None
    assert c.decide(0.95).action == 'OFF'

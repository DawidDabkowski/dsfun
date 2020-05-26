import pytest
from dsfun.f1_loss_tf import f1_loss_tf

#class TestF1LossTf:

def test_trivial_case():
    assert 1.0 == pytest.approx(f1_loss_tf())

import pytest
import tensorflow as tf
from dsfun import f1_loss

# class TestF1Loss(object):
    
@pytest.fixture
def zero(): 
    return tf.constant([[0.0]])
    
@pytest.fixture
def half():
    return tf.constant([[0.5]])

@pytest.fixture
def one():
    return tf.constant([[1.0]])
    
@pytest.fixture    
def y_true_vert():
    return tf.constant([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 1.0]])

@pytest.fixture
def y_pred_vert():
    return tf.constant([[0.5, 0.5], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]])

@pytest.fixture
def y_true_horiz(): 
    return tf.transpose(tf.constant([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 1.0]]))

@pytest.fixture
def y_pred_horiz():
    return tf.transpose(tf.constant([[0.5, 0.5], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]]))
    
def test_true_zero_pred_zero(zero):
    assert pytest.approx(1.0) == f1_loss(zero, zero, 'macro')
        
def test_true_zero_pred_one(zero, one):
    assert pytest.approx(1.0) == f1_loss(zero, one, 'micro')

def test_true_one_pred_zero(one, zero):
    assert pytest.approx(1.0) == f1_loss(one, zero, 'macro')

def test_true_one_pred_one(one):
    assert pytest.approx(0.0) == f1_loss(one, one, 'micro')

def test_true_zero_pred_half(zero, half):
    assert pytest.approx(1.0) == f1_loss(zero, half, 'micro')
    
def test_true_one_pred_half(one, half):
    assert pytest.approx(1/3) == f1_loss(one, half, 'macro')

def test_corner_preds_vert_macro(y_true_vert, y_pred_vert):
    assert pytest.approx(9/20) == f1_loss(y_true_vert, y_pred_vert, 'macro')

def test_corner_preds_vert_micro(y_true_vert, y_pred_vert):
    assert pytest.approx(4/9) == f1_loss(y_true_vert, y_pred_vert, 'micro')

def test_corner_preds_horiz_macro(y_true_horiz, y_pred_horiz):
    assert pytest.approx(11/24) == f1_loss(y_true_horiz, y_pred_horiz, 'macro')

def test_corner_preds_horiz_micro(y_true_horiz, y_pred_horiz):
    assert pytest.approx(4/9) == f1_loss(y_true_horiz, y_pred_horiz, 'micro')
        

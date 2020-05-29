import pytest
import tensorflow as tf
from dsfun import f1_loss

class TestF1LossTf(object):
    
    zero = tf.constant([[0]])
    half = tf.constant([[1/2]])
    one = tf.constant([[1]])
    
    y_true_vert = tf.constant([[1.0, 0.0], [1.0, 0.0]])
    y_pred_vert = tf.constant()
    y_true_horiz = tf.transpose(y_true_vert)
    y_pred_horiz = tf.transpose(y_pred_horiz)
    
    def test_true_zero_pred_zero(self):
        assert pytest.approx(1.0) == f1_loss(zero, zero, 'macro')
        
    def test_true_zero_pred_one(self):
        assert pytest.approx(0.0) == f1_loss(zero, one, 'micro')
        
    def test_true_one_pred_zero(self):
        assert pytest.approx(0.0) == f1_loss(one, zero, 'macro')
        
    def test_true_one_pred_one(self):
        assert pytest.approx(0.0) == f1_loss(one, one, 'micro')
        
    def test_true_one_pred_half(self):
        assert pytest.approx(2/3) == f1_loss(one, half, 'macro')
        
    def test_true_zero_pred_zero(self):
        assert pytest.approx(0.0) == f1_loss(zero, half, 'micro')
        
    def test_corner_preds_horiz_macro(self):
        assert pytest.approx(5/18) == f1_loss(y_true_horiz, y_pred_horiz, 'macro')
        
    def test_corner_preds_horiz_micro(self):
        assert pytest.approx(0.5) == f1_loss(y_true_horiz, y_pred_horiz, 'micro')

    def test_corner_preds_vert_macro(self):
        assert pytest.approx(0.5) == f1_loss(y_true_vert, y_pred_vert, 'macro')
        
    def test_corner_preds_vert_micro(self):
        assert pytest.approx(0.5) == f1_loss(y_true_vert, y_pred_vert, 'micro')
        
    def test_two_classes_three_rows(self):
        assert
        

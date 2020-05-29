import tensorflow as tf

def f1_loss(y_true, y_pred, mode='macro'):
    """Computes differentiable f1 loss fun nction.
    
    Notes:
    - By convention, loss is set to zero when formula is undefined.
    - Calculating f1 on small batch can give a very biased estimate."""
    pass

def f1_score(y_true, y_pred, mode='marcro'):
    y_pred = tf.math.round(y_pred)
    return 1 - f1_loss(y_true, y_pred, mode)
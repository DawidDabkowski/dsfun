import tensorflow as tf

def f1_loss(y_true, y_pred, mode='macro'):
    """Computes differentiable f1 loss fun nction.
    
    Notes:
    - By convention, loss is set to zero when formula is undefined.
    - Calculating f1 on small batch can give a very biased estimate."""
    
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.cast(y_pred, tf.float32)
    sum_axis = {'macro': 0, 'micro': None}[mode]
    
    tp = tf.reduce_sum(y_true * y_pred, axis=sum_axis)
    #tn = tf.reduce_sum((1 - y_true) * (1 - y_pred), axis=sum_axis)
    fp = tf.reduce_sum((1 - y_true) * y_pred, axis=sum_axis)
    fn = tf.reduce_sum(y_true * (1 - y_pred), axis=sum_axis)

    f1 = 2*tp / (2*tp + fn + fp + 1e-16)
    return 1.0 - tf.reduce_mean(f1, axis=sum_axis).numpy()


def f1_score(y_true, y_pred, mode='marcro'):
    y_pred = tf.math.round(y_pred)
    return 1.0 - f1_loss(y_true, y_pred, mode)
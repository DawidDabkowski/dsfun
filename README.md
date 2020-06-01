[![Build Status](https://travis-ci.com/DawidDabkowski/dsfun.svg?branch=master)](https://travis-ci.com/DawidDabkowski/dsfun) [![codecov](https://codecov.io/gh/DawidDabkowski/dsfun/branch/master/graph/badge.svg)](https://codecov.io/gh/DawidDabkowski/dsfun)


# DSfun

This package contains useful loss function class for training algorithms. These are f1-loss related functions. The main features:
- It is differentiable so it works with tensorflow
- It is more eficient than standard implementations
- Great for task that require to optimize F1-score
- Works with missing data *(TO DO)
- Can be modified to perform arbitrary differential functions on confusion matrix *(TO DO)*

Limitations:
- As any machine learning framework, this loss function shouldn't be used without proper validation as it is not deeply understood
- If calculating on batches, it will give a biased estimation of global loss
- If there are no representatives of a class in a batch, it might not converge properly

# Instalation

`pip install dsfun`

# Usage

*TO DO*

`import tensorflow as tf`

`from dsfun import f1_loss, f1_score`

`y_true = tf.constant([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 1.0]])`

`y_pred = tf.constant([[0.5, 0.5], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]])`

`f1_loss(y_true, y_pred, 'macro')`

`> ?`

`f1_score(y_true, y_pred, 'macro')`

`> ?`
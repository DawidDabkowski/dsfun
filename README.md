[![Build Status](https://travis-ci.com/DawidDabkowski/dsfun.svg?branch=master)](https://travis-ci.com/DawidDabkowski/dsfun) [![codecov](https://codecov.io/gh/DawidDabkowski/dsfun/branch/master/graph/badge.svg)](https://codecov.io/gh/DawidDabkowski/dsfun)


# DSfun

**This package is under development and limited for now. Eventually, it will contain a special categorical loss function class for training machine learning algorithms. The goal features include:**
- Wrapping in a simple interface for many useful loss functions based on confusion matrix
- Differentiability (compatibility with tensorflow)
- Scalable to multilabel problems
- Time efficiency optimizations
- Working with missing labels

Limitations:
- Loss function that aren't widely studied, should be used with caution and proper validation
- If calculating on batches, it might give a biased estimation of global loss
- As the class is broad, some of the functions might not converge at all

# Instalation

```
pip install dsfun
```

# Usage example

```
import tensorflow as tf
from dsfun import f1_loss, f1_score

y_true = tf.constant([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 1.0]])
y_pred = tf.constant([[0.5, 0.5], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]])

print(f1_loss(y_true, y_pred, 'macro'))
print(f1_score(y_true, y_pred, 'macro'))
```

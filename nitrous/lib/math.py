from __future__ import absolute_import
import math as _pymath
import ctypes

from .. import llvm
from . import IntrinsicEmitter, value_emitter

pi = _pymath.pi
e = _pymath.e


def exp(x):
    return IntrinsicEmitter("exp", x)


def log(x, base=None):

    @value_emitter
    def emit(module, builder):
        n, n_ty = IntrinsicEmitter("log", x)(module, builder)
        if base is not None:
            d, _ = IntrinsicEmitter("log", base)(module, builder)
            n = llvm.BuildFDiv(builder, n, d, "")
        return n, n_ty

    return emit


def sqrt(x):
    return IntrinsicEmitter("sqrt", x)


exp.__doc__ = _pymath.exp.__doc__
sqrt.__doc__ = _pymath.sqrt.__doc__
log.__doc__ = _pymath.log.__doc__

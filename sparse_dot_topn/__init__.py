# flake8: noqa
import sys
import warnings

# Filter out Cython harmless warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
warnings.filterwarnings("ignore", message="numpy.ndarray size changed")

if sys.version_info[0] >= 3:
    from sparse_dot_topn.awesome_cossim_topn import awesome_cossim_topn
else:
    from awesome_cossim_topn import awesome_cossim_topn

import os
import glob

# Get the modules in the current commands directory
modules = glob.glob(os.path.dirname(__file__) + '/*.py')

__all__ = [os.path.basename(f)[:-3] for f in modules
           if not os.path.basename(f).startswith('_')]

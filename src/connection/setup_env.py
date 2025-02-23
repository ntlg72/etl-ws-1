import sys
import os

def setup_pythonpath():
    # Add the 'src' directory to the PYTHONPATH
    sys.path.append(os.path.abspath('../src'))

def setup_environment():
    setup_pythonpath()
    print("Environment setup complete.")

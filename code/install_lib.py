import sys
from os.path import expanduser

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


""" # Install packages
install('matplotlib')
install('imblearn')
install('joblib')
install('pandas')
install('numpy')
install('shap')
install('scikit-learn')
install('xgboost') """


# Add site-packages to Python path
#sys.path.append(expanduser("~/.local/lib/python3.10/site-packages"))
sys.path.append(expanduser("/home/vscode/.local/lib/python3.10/site-packages"))
 
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

pytest_plugins = ['pytester']

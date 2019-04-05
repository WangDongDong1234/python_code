import sys
list=__file__.split("/")
base_path="/".join(list[:-2])
sys.path.append(base_path)
from core.main import fun
fun()
from pathlib import Path
from tclogger import OSEnver

configs_root = Path(__file__).parents[1] / "configs"
envs_path = configs_root / "envs.json"
ENVS_ENVER = OSEnver(envs_path)
DATA_PROXY_API_ENVS = ENVS_ENVER["data_proxy_api"]
CACHE_ROOT = Path(__file__).parents[1] / ENVS_ENVER["cache_root"]

import os
from fastapi import APIRouter
import glob
import importlib

API_VERSION = 1
ROUTER_PREFIX = f"v{API_VERSION}"  # -> v1
MODULE_NAME = "api." + ROUTER_PREFIX  # -> api.v1
MODULE_FILES_PATH = MODULE_NAME.replace(
    ".", os.sep
)  # -> api\v1 for Windows, api/v1 for Unix

router = APIRouter(prefix="/" + ROUTER_PREFIX, tags=[f"API {ROUTER_PREFIX}"])

module_files = glob.glob(f"{MODULE_FILES_PATH}/*.py")
module_names = [
    f"{MODULE_NAME}.{file.split(os.sep)[-1].split('.')[0]}"
    for file in filter(lambda x: not x.endswith("__init__.py"), module_files)
]
modules = [importlib.import_module(name) for name in module_names]

for module in modules:
    router.include_router(module.router)

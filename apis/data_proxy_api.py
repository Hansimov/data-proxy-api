import requests
import uvicorn

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from tclogger import logger
from typing import Optional

from apis.arg_parser import ArgParser
from configs.envs import DATA_PROXY_APP_ENVS


class DataProxyAPI:
    REQUESTS_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    def __init__(self, app_envs: dict = {}):
        self.title = app_envs.get("app_name")
        self.version = app_envs.get("version")
        self.app = FastAPI(
            docs_url="/",
            title=self.title,
            version=self.version,
            swagger_ui_parameters={"defaultModelsExpandDepth": -1},
        )
        # self.allow_cors()
        self.setup_routes()
        logger.success(f"> {self.title} - v{self.version}")

    def allow_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def get_img(self, url: str):
        response = requests.get(url, headers=self.REQUESTS_HEADERS)
        image_bytes = response.content
        return Response(content=image_bytes, media_type="image/jpeg")

    def setup_routes(self):
        self.app.get(
            "/img",
            summary="Get image by url",
        )(self.get_img)


if __name__ == "__main__":
    app_envs = DATA_PROXY_APP_ENVS
    app = DataProxyAPI(app_envs).app
    app_args = ArgParser(app_envs).args
    if app_args.reload:
        uvicorn.run("__main__:app", host=app_args.host, port=app_args.port, reload=True)
    else:
        uvicorn.run("__main__:app", host=app_args.host, port=app_args.port)

    # python -m apps.data_proxy_api
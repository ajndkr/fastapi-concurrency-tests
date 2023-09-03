import asyncio
import logging
import time
import uuid

import loguru
from fastapi import FastAPI


class GunicornHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger("gunicorn.error").handle(record)


logger = loguru.logger
logger.remove()
logger.add(
    GunicornHandler(),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO",
)


app = FastAPI()


@app.get("/sync")
def sync_endpoint():
    logger.info(f"New request - {str(uuid.uuid4())}")
    time.sleep(10)
    return {"message": "success"}


@app.get("/async")
async def async_endpoint():
    logger.info(f"New request - {str(uuid.uuid4())}")
    await asyncio.sleep(10)
    return {"message": "success"}

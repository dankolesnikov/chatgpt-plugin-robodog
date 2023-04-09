
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware

origins = ["https://chat.openai.com"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sit")
async def sit():
    """
    This endpoint is used to tell the robot to sit.
    It takes no parameters. 
    """
    try:
        return JSONResponse(content='OK', status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/dance")
async def dance():
    """
    This endpoint is used to tell the robot to do a dance.
    It takes no parameters. 
    """
    try:
        return JSONResponse(content='OK', status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/logo.png")
async def plugin_logo():
    return FileResponse('.well-known/dog_logo.png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open(".well-known/ai-plugin.json") as f:
        text = f.read()
        return JSONResponse(content=json.loads(text))
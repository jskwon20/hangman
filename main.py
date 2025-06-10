from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    return FileResponse("hangman.html")


# 모든 경로에 대해 index.html을 반환 (SPA 대응)
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse("hangman.html")


# Handle favicon.ico request
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

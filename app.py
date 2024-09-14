from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/api/hello")
def api_hello():
    return JSONResponse(content={"message": "Hello from the API!"})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)

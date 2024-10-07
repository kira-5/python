from fastapi import FastAPI
from app.api.v1.endpoints import example
import uvicorn

app = FastAPI()

# Include the router for the example endpoints
app.include_router(example.router, prefix="/api/v1/example", tags=["example"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

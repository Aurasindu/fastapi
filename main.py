from fastapi import FastAPI, Depends #import the FastAPI class from the FastAPI library, which will handle API requests and responses 
from fastapi.middleware.cors import CORSMiddleware
from routers import secure, public
from auth import get_user 
#from mangum import Mangum

app = FastAPI(
    title = "Food Save API",
    description = "API for application Food Save that supports zero food waste.",
    version = "1.0.0",
) #create an instance of FastAPI class and assign to variable app 

# Pengaktifan CORS 
app.add_middleware (
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(public.router, prefix="/api/v1/public", tags=["public"])
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    tags=["secure"],
    dependencies=[Depends(get_user)],
)

@app.get("/") #define a route (URL path that clients can use to access API)
async def hello(): # an asynchronous (async) function; using async in fastapi makes code faster when handling many requests at the same time
    return "Welcome to Food Save API"
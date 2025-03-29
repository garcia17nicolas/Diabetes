from fastapi import FastAPI

from routers import routerPreditions

app = FastAPI()
app.include_router(routerPreditions.router)

if __name__=="__main__":
    app.rum()
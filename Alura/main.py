from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello')
def ola_mundo():
    return {'Hello': 'World!'}
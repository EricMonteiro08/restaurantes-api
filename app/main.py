from fastapi import FastAPI

app = FastAPI(title="API Rede de Restaurantes")

@app.get("/")
def raiz():
    return {"mensagem": "API funcionando"}
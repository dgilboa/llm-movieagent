from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from neo4j_semantic_layer import agent_executor as neo4j_semantic_agent
from echo_server import agent_executor as echo_server

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, neo4j_semantic_agent, path="/movie-agent")
add_routes(app, echo_server, path="/echo-server")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

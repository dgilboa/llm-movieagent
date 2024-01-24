from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool

from dataclasses import asdict
from echo_server.ids import IDS


# working with local ids server Dan created
ids = IDS("http://localhost:8088")

def get_information(entity: str, type: str) -> str:
    if type == "vertex":
        res = ids.get_vertex(entity)
        print("Result we got from IDS :" + res.value)
        return f"id_type:{res.id_type} \n value:{res.value}"
    elif type == "edge":
        return "Edges information not yet supported"
    else:
        return "Unidentified type " + type

    # return "echo" + entity + " \n Type:"+type
    # candidates = get_candidates(entity, type)
    # print("Candidates: ", candidates)
    # if not candidates:
    #     return "No information was found about the movie or person in the database"
    # elif len(candidates) > 1:
    #     newline = "\n"
    #     return (
    #         "Need additional information, which of these "
    #         f"did you mean: {newline + newline.join(str(d) for d in candidates)}"
    #     )
    # data = graph.query(
    #     description_query, params={"candidate": candidates[0]["candidate"]}
    # )
    # print("get_info: ", data)
    # return data[0]["context"]


class InformationInput(BaseModel):
    entity: str = Field(description="vertex or an edge mentioned in the question")
    entity_type: str = Field(
        description="type of the entity. Available options are 'vertex' or 'edge'"
    )


class InformationTool(BaseTool):
    name = "Info"
    description = (
        "useful for when you need to answer questions about various vertices or edges"
    )
    args_schema: Type[BaseModel] = InformationInput

    def _run(
        self,
        entity: str,
        entity_type: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        return get_information(entity, entity_type)

    async def _arun(
        self,
        entity: str,
        entity_type: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        return get_information(entity, entity_type)

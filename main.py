from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Union
from model.recommender import recommend  # import from your recommender module

app = FastAPI()

# Define request schema
class RecommendRequest(BaseModel):
    roomtype: str
    country: str
    city: str
    property: str
    starrating: int
    user_id: Optional[Union[str,int]] = None

# Define POST endpoint
@app.post("/recommend")
def get_recommendations(req: RecommendRequest):
    recommendations = recommend(
        type=req.roomtype,
        country=req.country,
        city=req.city,
        property=req.property,
        starrating=req.starrating,
        user_id=req.user_id
    )
    return {"recommendations": recommendations}

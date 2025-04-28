from fastapi import APIRouter, Request, HTTPException # type: ignore
import modules.load_data
import modules.data_analysis

router = APIRouter()

# Carrega os dados
data_analysis = modules.data_analysis.DataAnalysis(modules.load_data.get_data())

@router.get("/users")
def get_users():
    return data_analysis.get_property_for_all_data("nome")

@router.get("/users/{property_name}")
def get_users_property(property_name: str):
    return data_analysis.get_property_for_all_data(property_name)

@router.get("/user/{user_id}")
def get_user_id(user_id: str):
    user = data_analysis.get_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

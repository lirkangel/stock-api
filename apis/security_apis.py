import grpc

from fastapi import APIRouter

app = APIRouter()


@app.get("/token/verify/")
def verify_token(token: str):
    # gRPC client for making RPC calls to the server
    response = {}
    data = {
        "user_id": response.user_id,
        "is_token_valid": response.token_valid
    }
    return data

from fastapi import APIRouter

from utils.stock_service import result_stock

router = APIRouter()


@router.get('/{stock_name}')
async def get_stock(stock_name: str):
    result = await result_stock(stock_name, 'information')
    return result

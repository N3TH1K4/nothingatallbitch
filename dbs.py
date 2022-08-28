import config as c
import codecs
import pickle
from string import ascii_lowercase
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from typing import Dict, List, Union

mongo_client = MongoClient(c.MONGO_URL)
db = mongo_client.ak
countdb = db.waifusasss

def obj_to_str(obj):
    if not obj:
        return False
    string = codecs.encode(pickle.dumps(obj), "base64").decode()
    return string


def str_to_obj(string: str):
    obj = pickle.loads(codecs.decode(string.encode(), "base64"))
    return obj

async def _get_filters(chat_id: int) -> Dict[str, int]:
    _filters = await countdb.find_one({"chat_id": chat_id})
    if not _filters:
        return {}
    return _filters["filters"]


async def get_filters_names(chat_id: int) -> List[str]:
    _filters = []
    for _filter in await _get_filters(chat_id):
        _filters.append(_filter)
    return _filters

async def get_filters_count(lol) -> dict:
    chats_count = 0
    filters_count = 0
    async for chat in countdb.find({"chat_id": lol}):
        filters_name = await get_filters_names(chat["chat_id"])
        filters_count += len(filters_name)
        chats_count += 1
    return {
        "chats_count": chats_count,
        "filters_count": filters_count,
    }


async def get_filter(chat_id: int, name: str,) -> Union[bool, dict]:
    name = name.lower().strip()
    _filters = await _get_filters(chat_id)
    if name in _filters:
        return _filters[name]
    return False


async def save_filter(chat_id: int, name: str, _filter: dict):
    name = name.strip()
    _filters = await _get_filters(chat_id)
    _filters[name] = _filter
    await countdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"filters": _filters}},
        upsert=True,
    )

async def check_dbs(cap: str,namer:str,chat_id: int, name: str, _filter: dict,no:str):
    no1 = "1️⃣"
    no2 = '2️⃣'
    no3 = '3️⃣'
    no4 = '4️⃣'
    no5 = '5️⃣'
    name = f"{no1}{cap}{no}"

        
async def delete_filter(chat_id: int, name: str,) -> bool:
    filtersd = await _get_filters(chat_id)
    name = name.strip()
    if name in filtersd:
        del filtersd[name]
        await countdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False

async def choosing_lvl(chat_id,cap,idm):
    no1 = f"1x {cap} ID: {idm}"
    no2 = f"2x {cap} ID: {idm}"
    no3 = f"3x {cap} ID: {idm}"
    no4 = f"4x {cap} ID: {idm}"
    no5 = f"5x {cap} ID: {idm}"
    no6 = f"6x {cap} ID: {idm}"
    no7 = f"7x {cap} ID: {idm}"
    no8 = f"8x {cap} ID: {idm}"
    no9 = f"9x {cap} ID: {idm}"
    no10 = f"10x {cap} ID: {idm}"
    _filters = await get_filters_names(chat_id)
    if no1 in _filters:
        name = no1
        await delete_filter(chat_id,name)
        name = no2
    elif no2 in _filters:
        name = no2
        await delete_filter(chat_id,name)
        name = no3
    elif no3 in _filters:
        name = no3
        await delete_filter(chat_id,name)
        name = no4
    elif no4 in _filters:
        name = no4
        await delete_filter(chat_id,name)
        name = no5
    elif no5 in _filters:
        name = no5
        await delete_filter(chat_id,name)
        name = no6
    elif no6 in _filters:
        name = no6
        await delete_filter(chat_id,name)
        name = no7
    elif no7 in _filters:
        name = no7
        await delete_filter(chat_id,name)
        name = no8
    elif no8 in _filters:
        name = no8
        await delete_filter(chat_id,name)
        name = no9
    elif no9 in _filters:
        name = no9
        await delete_filter(chat_id,name)
        name = no10
    elif no10 in _filters:
        name = no10
        await delete_filter(chat_id,name)
        name = no10
    else:
        name = no1
    _filter = {
        "data": name 
        }
    await save_filter(chat_id, name, _filter)
    
async def choosing_lvl_trade(chat_id,cap):
    name = cap
    _filter = {
        "data": name 
        }
    await save_filter(chat_id, name, _filter)

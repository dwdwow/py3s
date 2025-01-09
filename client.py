from enum import Enum
from typing import Any, TypeVar, TypedDict, List
import requests

public_base_url = "https://public-api.solscan.io"
pro_base_url = "https://pro-api.solscan.io/v2.0"

D = TypeVar("D")

RespData = TypedDict("RespData",{"success": bool,"data": List[D]})

Errors = TypedDict("Errors",{"code": int,"message": str})

RespError = TypedDict("RespError",{"success": bool,"errors": Errors})

ChainInfo = TypedDict("ChainInfo", {
    "blockHeight": int,
    "currentEpoch": int,
    "absoluteSlot": int,
    "transactionCount": int
})

class Flow(Enum):
    IN = "in"
    OUT = "out"
    
class SmallPageSize(Enum):
    PAGE_SIZE_10 = 10
    PAGE_SIZE_20 = 20
    PAGE_SIZE_30 = 30
    PAGE_SIZE_40 = 40
    
class LargePageSize(Enum):
    PAGE_SIZE_10 = 10
    PAGE_SIZE_20 = 20
    PAGE_SIZE_30 = 30
    PAGE_SIZE_40 = 40
    PAGE_SIZE_60 = 60
    PAGE_SIZE_100 = 100
    
class SortBy(Enum):
    BLOCK_TIME = "block_time"

class SortOrder(Enum):
    SORT_ORDER_ASC = "asc"
    SORT_ORDER_DESC = "desc"
    
class AccountActivityType(Enum):
    TRANSFER = "ACTIVITY_SPL_TRANSFER"
    BURN = "ACTIVITY_SPL_BURN"
    MINT = "ACTIVITY_SPL_MINT"
    CREATE_ACCOUNT = "ACTIVITY_SPL_CREATE_ACCOUNT"
    
class TokenType(Enum):
    TOKEN = "token"
    NFT = "nft"
    
class ActivityType(Enum):
    SWAP = "ACTIVITY_TOKEN_SWAP"
    AGG_SWAP = "ACTIVITY_AGG_TOKEN_SWAP"
    ADD_LIQUIDITY = "ACTIVITY_TOKEN_ADD_LIQ"
    REMOVE_LIQUIDITY = "ACTIVITY_TOKEN_REMOVE_LIQ"
    STAKE = "ACTIVITY_SPL_TOKEN_STAKE"
    UNSTAKE = "ACTIVITY_SPL_TOKEN_UNSTAKE"
    WITHDRAW_STAKE = "ACTIVITY_SPL_TOKEN_WITHDRAW_STAKE"
    MINT = "ACTIVITY_SPL_MINT"
    INIT_MINT = "ACTIVITY_SPL_INIT_MINT"

AccountTransfer = TypedDict("AccountTransfer", {
    "block_id": int,
    "trans_id": str,
    "block_time": int,
    "time": str,
    "activity_type": str,
    "from_address": str,
    "to_address": str,
    "token_address": str,
    "token_decimals": int,
    "amount": int,
    "flow": Flow
})

TokenAccount = TypedDict("TokenAccount", {
    "token_account": str,
    "token_address": str, 
    "amount": int,
    "token_decimals": int,
    "owner": str
})

Router = TypedDict("Router", {
    "token1": str,
    "token1_decimals": int,
    "amount1": str,
    "token2": str, 
    "token2_decimals": int,
    "amount2": str
})

AmountInfo = TypedDict("AmountInfo", {
    "token1": str,
    "token1_decimals": int,
    "amount1": int,
    "token2": str,
    "token2_decimals": int, 
    "amount2": int,
    "routers": List[Router]
})

DefiActivity = TypedDict("DefiActivity", {
    "block_id": int,
    "trans_id": str,
    "block_time": int,
    "time": str,
    "activity_type": ActivityType,
    "from_address": str,
    "to_address": str,
    "sources": List[str],
    "platform": str,
    "amount_info": AmountInfo
})



class Client:
    def __init__(self, auth_token: str):
        self.__headers = {"content-type": "application/json", "token": auth_token}
            
    def __init__(self, auth_token_file: str):
        with open(auth_token_file, "r") as f:
            auth_token = f.read()
            auth_token = auth_token.strip("\n\r\t ")
            self.__headers = {"content-type": "application/json", "token": auth_token}

    def get(self, base_url: str, path: str, kwargs: dict[str, Any]=None) -> RespData[D]:
        url = f"{base_url}/{path.lstrip('/')}"
        if kwargs:
            kvs = []
        for key, value in kwargs.items():
            if value is None:
                continue
            if key == "self":
                continue
            if key == "from_address":
                kvs.append(f"from={value}")
            elif key == "to_address":
                kvs.append(f"to={value}")
            elif isinstance(value, list):
                for v in value:
                    kvs.append(f"{key}[]={v}")
            elif isinstance(value, bool):
                kvs.append(f"{key}={str(value).lower()}")
            elif isinstance(value, Enum):
                kvs.append(f"{key}={value.value}")
            else:
                kvs.append(f"{key}={value}")
        if kvs:
            query_params = "&".join(kvs)
            url = f"{url}?{query_params}"
        resp = requests.get(url, headers=self.__headers)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 401:
            raise Exception("401: Unauthorized")
        elif resp.status_code == 403:
            raise Exception("403: Forbidden")
        elif resp.status_code == 404:
            raise Exception("404: Not Found")
        else:
            raise Exception(f"{resp.status_code}: {resp.text}")

    def chain_info(self) -> RespData[ChainInfo]:
        return self.get(public_base_url, "chaininfo")
    
    def account_transfers(self,
                           address: str,
                           activity_type: AccountActivityType = None,
                           token_account: str = None,
                           from_address: str = None,
                           to_address: str = None,
                           token_address: str = None,
                           amount_range: List[int] = None,
                           block_time_range: List[int] = None,
                           exclude_amount_zero: bool = False,
                           flow: Flow = None,
                           page: int = 1,
                           page_size: LargePageSize = LargePageSize.PAGE_SIZE_10,
                           sort_order: SortOrder = SortOrder.SORT_ORDER_DESC,
                           ) -> RespData[AccountTransfer]:
        args = locals()
        args["amount"] = args.pop("amount_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/transfer", args)
    
    def token_accounts(self,
                       address: str,
                       type: TokenType = TokenType.TOKEN,
                       page: int = 1,
                       page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10,
                       hide_zero: bool = False) -> RespData[TokenAccount]:
        return self.get(pro_base_url, "/account/token-accounts", locals())
    
    def defi_activities(self,
                        address: str,
                        activity_type: ActivityType = None,
                        from_address: str = None,
                        platform: List[str] = None,
                        source: List[str] = None,
                        token: str = None,
                        block_time_range: List[int] = None,
                        page: int = 1,
                        page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10,
                        sort_by: SortBy = SortBy.BLOCK_TIME,
                        sort_order: SortOrder = SortOrder.SORT_ORDER_DESC) -> RespData[DefiActivity]:
        args = locals()
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/defi/activities", args)



if __name__ == "__main__":
    client = Client("test_token.txt")
    print(client.defi_activities("E2X7eXU4Nqt27ZaBhRLkwX9xjzRKmtUZDcMRpkzLYjMt"))
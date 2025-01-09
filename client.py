from enum import Enum
from typing import Any, TypeVar, TypedDict, List
import requests

public_base_url = "https://public-api.solscan.io"
pro_base_url = "https://pro-api.solscan.io/v2.0"

D = TypeVar("D")

RespData = TypedDict("RespData",{"success": bool,"data": D})

Errors = TypedDict("Errors",{"code": int,"message": str})

RespError = TypedDict("RespError",{"success": bool,"errors": Errors})

ChainInfo = TypedDict("ChainInfo", {
    "blockHeight": int,
    "currentEpoch": int,
    "absoluteSlot": int,
    "transactionCount": int
})

class Flow(Enum):
    # Account Activity
    IN = "in"
    OUT = "out"
    # Token Activity
    EMPTY = ""
    
class TinyPageSize(Enum):
    PAGE_SIZE_12 = 12
    PAGE_SIZE_24 = 24
    PAGE_SIZE_36 = 36

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
    
class MarketSortBy(Enum):
    VOLUME = "volume"
    TRADE = "trade"
    
class TokenSortBy(Enum):
    PRICE = "price"
    HOLDER = "holder"
    MARKET_CAP = "market_cap" 
    CREATED_TIME = "created_time"
    
class NFTCollectionSortBy(Enum):
    ITEMS = "items"
    FLOOR_PRICE = "floor_price"
    VOLUMES = "volumes"
    
class NFTCollectionItemSortBy(Enum):
    LAST_TRADE = "last_trade"
    LISTING_PRICE = "listing_price"

class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"
    
class AccountActivityType(Enum):
    TRANSFER = "ACTIVITY_SPL_TRANSFER"
    BURN = "ACTIVITY_SPL_BURN"
    MINT = "ACTIVITY_SPL_MINT"
    CREATE_ACCOUNT = "ACTIVITY_SPL_CREATE_ACCOUNT"
    
class TokenType(Enum):
    TOKEN = "token"
    NFT = "nft"
    
class ActivityType(Enum):
    # Account Activity
    ACCOUNT_ACTIVITY_SWAP = "ACTIVITY_TOKEN_SWAP"
    ACCOUNT_ACTIVITY_AGG_SWAP = "ACTIVITY_AGG_TOKEN_SWAP"
    ACCOUNT_ACTIVITY_ADD_LIQUIDITY = "ACTIVITY_TOKEN_ADD_LIQ"
    ACCOUNT_ACTIVITY_REMOVE_LIQUIDITY = "ACTIVITY_TOKEN_REMOVE_LIQ"
    ACCOUNT_ACTIVITY_STAKE = "ACTIVITY_SPL_TOKEN_STAKE"
    ACCOUNT_ACTIVITY_UNSTAKE = "ACTIVITY_SPL_TOKEN_UNSTAKE"
    ACCOUNT_ACTIVITY_WITHDRAW_STAKE = "ACTIVITY_SPL_TOKEN_WITHDRAW_STAKE"
    ACCOUNT_ACTIVITY_MINT = "ACTIVITY_SPL_MINT"
    ACCOUNT_ACTIVITY_INIT_MINT = "ACTIVITY_SPL_INIT_MINT"
    # Token Activity
    TOKEN_ACTIVITY_TRANSFER = "ACTIVITY_SPL_TRANSFER"
    TOKEN_ACTIVITY_BURN = "ACTIVITY_SPL_BURN" 
    TOKEN_ACTIVITY_MINT = "ACTIVITY_SPL_MINT"
    TOKEN_ACTIVITY_CREATE_ACCOUNT = "ACTIVITY_SPL_CREATE_ACCOUNT"
    
class NFTActivityType(Enum):
    SOLD = "ACTIVITY_NFT_SOLD"
    LISTING = "ACTIVITY_NFT_LISTING"
    BIDDING = "ACTIVITY_NFT_BIDDING"
    CANCEL_BID = "ACTIVITY_NFT_CANCEL_BID"
    CANCEL_LIST = "ACTIVITY_NFT_CANCEL_LIST"
    REJECT_BID = "ACTIVITY_NFT_REJECT_BID"
    UPDATE_PRICE = "ACTIVITY_NFT_UPDATE_PRICE"
    LIST_AUCTION = "ACTIVITY_NFT_LIST_AUCTION"

class BalanceChangeType(Enum):
    INC = "inc"
    DEC = "dec"
    
class TxStatus(Enum):
    SUCCESS = "Success"
    FAIL = "Fail"

class StakeRole(Enum):
    STAKER = "staker"
    WITHDRAWER = "withdrawer"
    
class StakeAccountStatus(Enum):
    ACTIVE = "active"
    
class StakeAccountType(Enum):
    ACTIVE = "active"
    
class AccountType(Enum):
    SYSTEM_ACCOUNT = "system_account"
    
class TxFilter(Enum):
    EXCEPT_VOTE = "exceptVote"
    ALL = "all"

Transfer = TypedDict("AccountTransfer", {
    "block_id": int,
    "trans_id": str,
    "block_time": int,
    "time": str,
    "activity_type": ActivityType,
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

ChildRouter = TypedDict("ChildRouter", {
    "token1": str,
    "token1_decimals": int,
    "amount1": str,
    "token2": str, 
    "token2_decimals": int,
    "amount2": str,
})

Router = TypedDict("Router", {
    "token1": str,
    "token1_decimals": int,
    "amount1": str,
    "token2": str, 
    "token2_decimals": int,
    "amount2": str,
    "child_routers": List[ChildRouter]
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
    "amount_info": AmountInfo,
    "routers": List[Router]
})

AccountChangeActivity = TypedDict("AccountChangeActivity", {
    "block_id": int,
    "block_time": int,
    "time": str,
    "trans_id": str,
    "address": str,
    "token_address": str,
    "token_account": str,
    "token_decimals": int,
    "amount": int,
    "pre_balance": int,
    "post_balance": int,
    "change_type": BalanceChangeType,
    "fee": int
})

ParsedCancelAllAndPlaceOrders = TypedDict("ParsedCancelAllAndPlaceOrders", {
    "type": str,
    "program": str,
    "program_id": str
})

Transaction = TypedDict("Transaction", {
    "slot": int,
    "fee": int,
    "status": TxStatus,
    "signer": List[str],
    "block_time": int,
    "tx_hash": str,
    "parsed_instructions": List[ParsedCancelAllAndPlaceOrders],
    "program_ids": List[str],
    "time": str
})

AccountStake = TypedDict("AccountStake", {
    "amount": int,
    "role": List[StakeRole],
    "status": StakeAccountStatus,
    "type": StakeAccountType,
    "voter": str,
    "active_stake_amount": int,
    "delegated_stake_amount": int,
    "sol_balance": int,
    "total_reward": str,
    "stake_account": str,
    "activation_epoch": int,
    "stake_type": int
})

AccountDetail = TypedDict("AccountDetail", {
    "account": str,
    "lamports": int,
    "type": AccountType,
    "executable": bool,
    "owner_program": str,
    "rent_epoch": int,
    "is_oncurve": bool
})

Market = TypedDict("Market", {
    "pool_id": str,
    "program_id": str,
    "token_1": str,
    "token_2": str,
    "token_account_1": str,
    "token_account_2": str,
    "total_trades_24h": int,
    "total_trades_prev_24h": int,
    "total_volume_24h": float,
    "total_volume_prev_24h": float
})

Token = TypedDict("Token", {
    "address": str,
    "decimals": int,
    "name": str,
    "symbol": str,
    "market_cap": float,
    "price": float,
    "price_24h_change": float,
    "created_time": int
})

TokenPrice = TypedDict("TokenPrice", {
    "date": int, # yyyymmdd
    "price": float
})

TokenHolder = TypedDict("TokenHolder", {
    "address": str,
    "amount": int,
    "decimals": int,
    "owner": str,
    "rank": int
})

TokenMeta = TypedDict("TokenMeta", {
    "supply": str,
    "address": str,
    "name": str,
    "symbol": str,
    "icon": str,
    "decimals": int,
    "holder": int,
    "creator": str,
    "create_tx": str,
    "created_time": int,
    "first_mint_tx": str,
    "first_mint_time": int,
    "price": float,
    "volume_24h": float,
    "market_cap": float,
    "market_cap_rank": int,
    "price_change_24h": float
})

TokenTop = TypedDict("TokenTop", {
    "address": str,
    "decimals": int,
    "name": str,
    "symbol": str,
    "market_cap": float,
    "price": float,
    "price_24h_change": float,
    "created_time": int
})

AccountKey = TypedDict("AccountKey", {
    "pubkey": str,
    "signer": bool,
    "source": str,
    "writable": bool
})

TransferInfo = TypedDict("TransferInfo", {
    "source_owner": str,
    "source": str,
    "destination": str,
    "destination_owner": str,
    "transfer_type": str,
    "token_address": str,
    "decimals": int,
    "amount_str": str,
    "amount": int,
    "program_id": str,
    "outer_program_id": str,
    "ins_index": int,
    "outer_ins_index": int,
    "event": str,
    "fee": dict
})

InstructionData = TypedDict("InstructionData", {
    "ins_index": int,
    "parsed_type": str,
    "type": str,
    "program_id": str,
    "program": str,
    "outer_program_id": str | None,
    "outer_ins_index": int,
    "data_raw": str | dict,
    "accounts": List[str],
    "activities": List[dict],
    "transfers": List[TransferInfo],
    "program_invoke_level": int
})

BalanceChange = TypedDict("BalanceChange", {
    "address": str,
    "pre_balance": str,
    "post_balance": str,
    "change_amount": str
})

TokenBalanceChange = TypedDict("TokenBalanceChange", {
    "address": str,
    "change_type": str,
    "change_amount": str,
    "decimals": int,
    "post_balance": str,
    "pre_balance": str,
    "token_address": str,
    "owner": str,
    "post_owner": str,
    "pre_owner": str
})

TransactionDetail = TypedDict("TransactionDetail", {
    "block_id": int,
    "fee": int,
    "reward": List[Any],
    "sol_bal_change": List[BalanceChange],
    "token_bal_change": List[TokenBalanceChange],
    "tokens_involved": List[str],
    "parsed_instructions": List[InstructionData],
    "programs_involved": List[str],
    "signer": List[str],
    "status": int,
    "account_keys": List[AccountKey],
    "compute_units_consumed": int,
    "confirmations": int | None,
    "version": str,
    "tx_hash": str,
    "block_time": int,
    "log_message": List[str],
    "recent_block_hash": str,
    "tx_status": str
})

TxActionData = TypedDict("TxActionData", {
    "amm_id": str,
    "amm_authority": str | None,
    "account": str,
    "token_1": str,
    "token_2": str,
    "amount_1": int,
    "amount_1_str": str,
    "amount_2": int,
    "amount_2_str": str,
    "token_decimal_1": int,
    "token_decimal_2": int,
    "token_account_1_1": str,
    "token_account_1_2": str,
    "token_account_2_1": str,
    "token_account_2_2": str,
    "owner_1": str,
    "owner_2": str
})

TxAction = TypedDict("TxAction", {
    "name": str,
    "activity_type": str,
    "program_id": str,
    "data": TxActionData,
    "ins_index": int,
    "outer_ins_index": int,
    "outer_program_id": str | None
})

TxActionTransfer = TypedDict("TxActionTransfer", {
    "source_owner": str,
    "source": str,
    "destination": str,
    "destination_owner": str,
    "transfer_type": str,
    "token_address": str,
    "decimals": int,
    "amount_str": str,
    "amount": int,
    "program_id": str,
    "outer_program_id": str,
    "ins_index": int,
    "outer_ins_index": int
})

# Update TransactionAction to match the actual response
TransactionAction = TypedDict("TransactionAction", {
    "tx_hash": str,
    "block_id": int,
    "block_time": int,
    "time": str,
    "fee": int,
    "transfers": List[TxActionTransfer],
    "activities": List[TxAction]
})

BlockDetail = TypedDict("BlockDetail", {
    "fee_rewards": int,
    "transactions_count": int,
    "current_slot": int,
    "block_height": int,
    "block_time": int,
    "time": str,
    "block_hash": str,
    "parent_slot": int,
    "previous_block_hash": str
})

PoolMarket = TypedDict("PoolMarket", {
    "pool_address": str,
    "program_id": str,
    "token1": str,
    "token1_account": str, 
    "token2": str,
    "token2_account": str,
    "total_volume_24h": int,
    "total_trade_24h": int,
    "created_time": int
})

PoolMarketInfo = TypedDict("PoolMarketInfo", {
    "pool_address": str,
    "program_id": str,
    "token1": str,
    "token2": str,
    "token1_account": str,
    "token2_account": str,
    "token1_amount": float,
    "token2_amount": float
})

PoolMarketDayVolume = TypedDict("PoolMarketDayVolume", {
    "day": int, # yyyymmdd
    "volume": float,
})

PoolMarketVolume = TypedDict("PoolMarketVolume", {
    "pool_address": str,
    "program_id": str,
    "total_volume_24h": int,
    "total_volume_change_24h": float,
    "total_trades_24h": int, 
    "total_trades_change_24h": float,
    "days": List[PoolMarketDayVolume]
})

APIUsage = TypedDict("APIUsage", {
    "remaining_cus": int,
    "usage_cus": int, 
    "total_requests_24h": int,
    "success_rate_24h": float,
    "total_cu_24h": int
})

NFTCreator = TypedDict("NFTCreator", {
    "address": str,
    "verified": int,
    "share": int
})

NFTFile = TypedDict("NFTFile", {
    "uri": str,
    "type": str
})

NFTProperties = TypedDict("NFTProperties", {
    "files": List[NFTFile],
    "category": str
})

NFTAttribute = TypedDict("NFTAttribute", {
    "trait_type": str,
    "value": str
})

NFTMetadata = TypedDict("NFTMetadata", {
    "image": str,
    "tokenId": int,
    "name": str,
    "symbol": str,
    "description": str,
    "seller_fee_basis_points": int,
    "edition": int,
    "attributes": List[NFTAttribute],
    "properties": NFTProperties,
    "retried": int
})

NFTData = TypedDict("NFTData", {
    "name": str,
    "symbol": str,
    "uri": str,
    "sellerFeeBasisPoints": int,
    "creators": List[NFTCreator],
    "id": int
})

NFTInfo = TypedDict("NFTInfo", {
    "address": str,
    "collection": str,
    "collectionId": str,
    "collectionKey": str,
    "createdTime": int,
    "data": NFTData,
    "meta": NFTMetadata,
    "mintTx": str
})

NFTActivity = TypedDict("NFTActivity", {
    "block_id": int,
    "trans_id": str, 
    "block_time": int,
    "time": str,
    "activity_type": NFTActivityType,
    "from_address": str,
    "to_address": str,
    "token_address": str,
    "marketplace_address": str,
    "collection_address": str,
    "amount": int,
    "price": int,
    "currency_token": str,
    "currency_decimals": int
})

NFTCollection = TypedDict("NFTCollection", {
    "collection_id": str,
    "name": str,
    "symbol": str,
    "floor_price": float,
    "items": int,
    "marketplaces": List[str],
    "volumes": float,
    "total_vol_prev_24h": float
})

NFTTradeInfo = TypedDict("NFTTradeInfo", {
    "trade_time": int,
    "signature": str,
    "market_id": str,
    "type": str,
    "price": str,
    "currency_token": str,
    "currency_decimals": int,
    "seller": str,
    "buyer": str
})

NFTCollectionMeta = TypedDict("NFTCollectionMeta", {
    "name": str,
    "family": str
})

NFTMetaProperties = TypedDict("NFTMetaProperties", {
    "files": List[NFTFile],
    "category": str,
    "creators": List[NFTCreator]
})

NFTItemMetadata = TypedDict("NFTItemMetadata", {
    "name": str,
    "symbol": str,
    "description": str,
    "seller_fee_basis_points": int,
    "image": str,
    "external_url": str,
    "collection": NFTCollectionMeta,
    "attributes": List[NFTAttribute],
    "properties": NFTMetaProperties
})

NFTItemData = TypedDict("NFTItemData", {
    "name": str,
    "symbol": str,
    "uri": str,
    "sellerFeeBasisPoints": int,
    "creators": List[NFTCreator],
    "id": int
})

NFTItemInfo = TypedDict("NFTItemInfo", {
    "address": str,
    "token_name": str,
    "token_symbol": str,
    "collection_id": str,
    "data": NFTItemData,
    "meta": NFTItemMetadata,
    "mint_tx": str,
    "created_time": int
})

NFTCollectionItem = TypedDict("NFTCollectionItem", {
    "tradeInfo": NFTTradeInfo,
    "info": NFTItemInfo
})

class Client:
    def __init__(self, auth_token: str):
        self.__headers = {"content-type": "application/json", "token": auth_token}
            
    def __init__(self, auth_token_file: str):
        with open(auth_token_file, "r") as f:
            auth_token = f.read()
            auth_token = auth_token.strip("\n\r\t ")
            self.__headers = {"content-type": "application/json", "token": auth_token}

    def get(self, base_url: str, path: str, kwargs: dict[str, Any]=None, export: bool = False) -> D:
        url = f"{base_url}/{path.lstrip('/')}"
        if kwargs:
            kvs = []
        for key, value in kwargs.items():
            if value is None or key == "self":
                continue
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
            if export:
                return resp.content
            else:
                return resp.json()["data"]
        elif resp.status_code == 401:
            raise Exception("401: Unauthorized")
        elif resp.status_code == 403:
            raise Exception("403: Forbidden")
        elif resp.status_code == 404:
            raise Exception("404: Not Found")
        elif resp.status_code == 429:
            raise Exception("429: Too Many Requests")
        elif resp.status_code == 500:
            raise Exception("500: Internal Server Error")
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
                           token: str = None,
                           amount_range: List[int] = None,
                           block_time_range: List[int] = None,
                           exclude_amount_zero: bool = False,
                           flow: Flow = None,
                           page: int = 1,
                           page_size: LargePageSize = LargePageSize.PAGE_SIZE_10,
                           sort_order: SortOrder = SortOrder.DESC,
                           ) -> List[Transfer]:
        args = locals()
        args["from"] = args.pop("from_address")
        args["to"] = args.pop("to_address")
        args["amount"] = args.pop("amount_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/transfer", args)
    
    def account_token_accounts(self,
                       address: str,
                       type: TokenType = TokenType.TOKEN,
                       page: int = 1,
                       page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10,
                       hide_zero: bool = False) -> List[TokenAccount]:
        return self.get(pro_base_url, "/account/token-accounts", locals())
    
    def account_defi_activities(self,
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
                        sort_order: SortOrder = SortOrder.DESC) -> List[DefiActivity]:
        args = locals()
        args["from"] = args.pop("from_address")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/defi/activities", args)
    
    def account_balance_changes(self,
                        address: str,
                        token: str = None,
                        amount_range: List[int] = None,
                        block_time_range: List[int] = None,
                        page: int = 1,
                        page_size: LargePageSize = LargePageSize.PAGE_SIZE_10,
                        remove_spam: bool = True,
                        flow: Flow = None,
                        sort_by: SortBy = SortBy.BLOCK_TIME,
                        sort_order: SortOrder = SortOrder.DESC) -> List[AccountChangeActivity]:
        args = locals()
        args["amount"] = args.pop("amount_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/balance_change", args)
    
    def account_transactions(self, address: str, limit: SmallPageSize=SmallPageSize.PAGE_SIZE_10) -> List[Transaction]:
        return self.get(pro_base_url, "/account/transactions", locals())
    
    def account_stakes(self, address: str, page: int = 1, page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10) -> List[AccountStake]:
        return self.get(pro_base_url, "/account/stake", locals())
    
    def account_detail(self, address: str) -> AccountDetail:
        return self.get(pro_base_url, "/account/detail", locals())
    
    def account_rewards_export(self, address:str, time_from:int, time_to:int) -> bytes:
        return self.get(pro_base_url, "/account/reward/export", locals(), export=True)
                             
    def account_transfer_export(self, 
                                address:str,
                                activity_type:AccountActivityType = None,
                                token_account:str = None,
                                from_address:str = None,
                                to_address:str = None,
                                token:str = None,
                                amount_range:List[int] = None,
                                block_time_range:List[int] = None,
                                exclude_amount_zero:bool=False,
                                flow: Flow = None) -> bytes:
        args = locals()
        args["amount"] = args.pop("amount_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/account/transfer/export", args, export=True)
    
    def token_trasfers(self,
                       address:str,
                       activity_type:ActivityType = None,
                       from_address:str = None,
                       to_address:str = None,
                       amount_range:List[int] = None,
                       block_time_range:List[int] = None,
                       exclude_amount_zero:bool=False,
                       page:int = 1,
                       page_size:LargePageSize = LargePageSize.PAGE_SIZE_10,
                       sort_by:SortBy = SortBy.BLOCK_TIME,
                       sort_order:SortOrder = SortOrder.DESC) -> List[Transfer]:
        args = locals()
        args["from"] = args.pop("from_address")
        args["to"] = args.pop("to_address")
        args["amount"] = args.pop("amount_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/token/transfer", args)

    def token_defi_activities(self,
                             address:str,
                             from_address:str = None,
                             platform:List[str] = None,
                             source:List[str] = None,
                             activity_type:ActivityType = None,
                             token:str = None,
                             block_time_range:List[int] = None,
                             page:int = 1,
                             page_size:LargePageSize = LargePageSize.PAGE_SIZE_10,
                             sort_by:SortBy = SortBy.BLOCK_TIME,
                             sort_order:SortOrder = SortOrder.DESC) -> List[DefiActivity]:
        args = locals()
        args["from"] = args.pop("from_address")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/token/defi/activities", args)
    
    def token_markets(self,
                      token_pair:List[str],
                      sort_by:MarketSortBy = MarketSortBy.VOLUME,
                      program:str = None,
                      page:int = 1,
                      page_size:LargePageSize = LargePageSize.PAGE_SIZE_100) -> List[Market]:
        args = locals()
        args["token"] = args.pop("token_pair")
        return self.get(pro_base_url, "/token/markets", args)

    def token_list(self,
                   sort_by:TokenSortBy = TokenSortBy.PRICE,
                   sort_order:SortOrder = SortOrder.DESC,
                   page:int = 1,
                   page_size:LargePageSize = LargePageSize.PAGE_SIZE_100) -> List[Token]:
        return self.get(pro_base_url, "/token/list", locals())
    
    def token_trending(self, limit:int = 10) -> List[Token]:
        return self.get(pro_base_url, "/token/trending", locals())

    def token_price(self, address: str, time_range: List[int] = None) -> List[TokenPrice]:
        """Get token price history.
        
        Args:
            address (str): Token address
            time_range (List[int], optional): Time range in yyyymmdd. Defaults to None.
                If provided, must be a list of 2 yyyymmdd [start_time, end_time].
                
        Returns:
            List[TokenPrice]: List of token prices with dates
            
        Example:
            >>> client.token_price("HeLp6NuQkmYB4pYWo2zYs22mESHXPQYzXbB8n4V98jwC")
            return real-time price

            >>> # Get prices between Jan 1 2022 and Jan 7 2022
            >>> client.token_price("HeLp6NuQkmYB4pYWo2zYs22mESHXPQYzXbB8n4V98jwC", 
            ...                   [20250101, 20250102])
            [{'date': 20250101, 'price': 2.1796472}, {'date': 20250102, 'price': 2.34}]
        """
        args = locals()
        args["time"] = args.pop("time_range")
        return self.get(pro_base_url, "/token/price", args)
    
    def token_holders(self,
                        address: str,
                        page: int = 1,
                        page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10,
                        from_amount: str=None,
                        to_amount: str=None) -> List[TokenHolder]:
        return self.get(pro_base_url, "/token/holders", locals())
    
    def token_meta(self, address: str) -> TokenMeta:
        return self.get(pro_base_url, "/token/meta", locals())
    
    def token_top(self) -> List[TokenTop]:
        return self.get(pro_base_url, "/token/top", locals())
    
    def tx_last(self, limit: LargePageSize = LargePageSize.PAGE_SIZE_10, filter: TxFilter = TxFilter.ALL) -> List[Transaction]:
        return self.get(pro_base_url, "/transaction/last", locals())

    def tx_detail(self, tx: str) -> TransactionDetail:
        return self.get(pro_base_url, "/transaction/detail", locals())
    
    def tx_actions(self, tx: str) -> TransactionAction:
        return self.get(pro_base_url, "/transaction/actions", locals())

    def block_last(self, limit: LargePageSize=LargePageSize.PAGE_SIZE_100) -> BlockDetail:
        return self.get(pro_base_url, "/block/last", locals())

    def block_transactions(self, block: int, page: int = 1, page_size: LargePageSize = LargePageSize.PAGE_SIZE_100) -> List[Transaction]:
        return self.get(pro_base_url, "/block/transactions", locals())

    def block_detail(self, block: int) -> BlockDetail:
        return self.get(pro_base_url, "/block/detail", locals())
    
    def pool_market_list(self,
                         sort_by: str = "created_time",
                         sort_order: SortOrder = SortOrder.DESC,
                         page: int = 1,
                         page_size: LargePageSize = LargePageSize.PAGE_SIZE_100, 
                         program: str = None,
                         ) -> List[PoolMarket]:
        return self.get(pro_base_url, "/market/list", locals())
    
    def pool_market_info(self, address: str) -> PoolMarketInfo:
        return self.get(pro_base_url, "/market/info", locals())
    
    def pool_market_volume(self, address: str, time_range: List[int] = None) -> PoolMarketVolume:
        args = locals()
        args["time"] = args.pop("time_range")
        return self.get(pro_base_url, "/market/volume", args)

    def api_usage(self) -> APIUsage:
        return self.get(pro_base_url, "/monitor/usage", locals())

    def news_nft(self, filter: str = "created_time", page: int = 1, page_size: TinyPageSize = TinyPageSize.PAGE_SIZE_12) -> List[NFTInfo]:
        return self.get(pro_base_url, "/nft/news", locals())
    
    def nft_activity(self,
                    from_address: str = None,
                    to_address: str = None,
                    source: List[str] = None,
                    activity_type: NFTActivityType = None,
                    token: str = None,
                    collection: str = None,
                    currency_token: str = None,
                    price_range: List[float] = None,
                    block_time_range: List[int] = None,
                    page: int = 1,
                    page_size: LargePageSize = LargePageSize.PAGE_SIZE_100) -> List[NFTActivity]:
        args = locals()
        args["from"] = args.pop("from_address")
        args["to"] = args.pop("to_address")
        args["price"] = args.pop("price_range")
        args["block_time"] = args.pop("block_time_range")
        return self.get(pro_base_url, "/nft/activity", locals())

    def nft_collection_list(self,
                             sort_by: NFTCollectionSortBy = NFTCollectionSortBy.FLOOR_PRICE,
                             sort_order: SortOrder = SortOrder.DESC,
                             page: int = 1,
                             page_size: SmallPageSize = SmallPageSize.PAGE_SIZE_10,
                             collection: str = None,
                             ) -> List[NFTCollection]:
        return self.get(pro_base_url, "/nft/collection/lists", locals())
    
    def nft_collection_items(self,
                             collection: str,
                             sort_by: NFTCollectionItemSortBy = NFTCollectionItemSortBy.LAST_TRADE,
                             page: int = 1,
                             page_size: TinyPageSize = TinyPageSize.PAGE_SIZE_12,
                             ) -> List[NFTCollectionItem]:
        return self.get(pro_base_url, "/nft/collection/items", locals())


if __name__ == "__main__":
    client = Client("test_token.txt")
    print(client.nft_collection_items("fc8dd31116b25e6690d83f6fb102e67ac6a9364dc2b96285d636aed462c4a983"))

from typing import TypeVar, TypedDict, List
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

class Client:
    def __init__(self, auth_token: str):
        self.__headers = {"content-type": "application/json", "token": auth_token}
            
    def __init__(self, auth_token_file: str):
        with open(auth_token_file, "r") as f:
            auth_token = f.read()
            auth_token = auth_token.strip("\n\r\t ")
            self.__headers = {"content-type": "application/json", "token": auth_token}

    def get(self, base_url: str, path: str, **kwargs) -> RespData[D]:
        url = f"{base_url}/{path.lstrip('/')}"

        if kwargs:
            query_params = "&".join(f"{key}={value}" for key, value in kwargs.items())
            url = f"{url}?{query_params}"

        resp = requests.get(url, headers=self.__headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            errors = resp.json()
            raise Exception(f"{resp.status_code}: {errors}")

    def chain_info(self) -> RespData[ChainInfo]:
        return self.get(public_base_url, "chaininfo")


if __name__ == "__main__":
    client = Client("test_token.txt")
    print(client.chain_info())

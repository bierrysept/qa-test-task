
import pytest
from src.main import site_popularity
from typing import Union

@pytest.mark.parametrize(
    "num",
    [
        10**7,
        1.5 * 10**7,
        5 * 10**7,
        10**8,
        5 * 10**8,
        10**9,
        1.5 * 10**9
    ] 
)
def test_popularity(num: int):
    for i in site_popularity:
        assert num <= int(i["populatity"]), get_popularity_error_message(i, num)

def get_popularity_error_message(row: dict[str, Union[str, int]], expected_popularity: int)->str:
    #Example: “Wikipedia (Frontend:JavaScript|Backend:PHP) has 475 000 000 unique visitors per month. (Expected more than 500 000 000)”
    name = str(row["website"])
    frontend_stack  = str(row["frontend"])
    backend_stack = str(row["backend"])
    popularity = str(row["populatity"])
    return f"{name} (Frontend:{frontend_stack}|Backend:{backend_stack}) has {popularity} unique visitors per month. (Expected more than {expected_popularity})"
    
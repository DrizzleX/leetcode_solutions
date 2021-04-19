import pytest
from defanging_an_ip_address import Solution
test_data_set = [
    ("1.2.3.4", "1[.]2[.]3[.]4")
]

@pytest.mark.parametrize("ip_addr, expected", test_data_set)
def test_solution(ip_addr, expected):
    solution = Solution()
    assert expected == solution.defangIPaddr(ip_addr)


import unittest
import requests

def make_expr_request(expression, expected_value):
    result = requests.get("http://localhost:8080/expr/"+str(expression))
    if result.status_code != 200:
        return "None"
    assert 'json' in result.headers['Content-Type']
    data = result.json()
    assert data['value'] == expected_value
    
class Service_TestCase(unittest.TestCase):
    def test_000_do_nothing(self):
        pass
    
    def test_001_test_simple_expression(self):
        make_expr_request(0.05,"5E-02")
        make_expr_request(0.001,"1E-03")
        #make_expr_request("1",1)

    def test_002_test_simple_expression(self):
        make_expr_request("0.05","5E-02")
        make_expr_request("0.001","1E-03")

    def test_003_test_simple_expression(self):
        make_expr_request("5123","5.123E+03")
        make_expr_request("12.34","1.234E+01")    

if __name__ == "__main__":
    unittest.main(verbosity=2)
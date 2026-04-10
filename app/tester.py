# this file actually test APIs
# for each test case, it calls the API and checks the respons status and marks it as pass or fail
import requests


def run_test_cases(url, test_cases):
    results = []
    for test in test_cases:
        try:
            response = requests.request(method=test["method"], url=url)
            result = {
                "name": test["name"],
                "expected_status": test["expected_status"],
                "actual_status": response.status_code,
                "pass": response.status_code == test["expected_status"],
            }
        except Exception as e:
            result = {"name": test["name"], "error": str(e), "pass": False}

        results.append(result)
    return results

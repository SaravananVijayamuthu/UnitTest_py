try:
    import unittest
    from run import app
except Exception as e:
    print(format(e))

#Test through api status
class TestAPI(unittest.TestCase):
    def test1(self):
        tester = app.test_client(self)
        response  = tester.get("/hi")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
        

if __name__ == "__main__":
    unittest.main()

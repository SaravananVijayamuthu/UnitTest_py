try:
    import unittest
    from run import app
except Exception as e:
    print(format(e))

# Test through api status
class TestAPI(unittest.TestCase):
    def test1(self):
        tester = app.test_client(self)
        response = tester.get("/hi")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check content
    def test1_content(self):
        tester = app.test_client(self)
        response = tester.get("/hi")
        self.assertEqual(response.content_type, "application/json")

    # Data
    def test1_Data(self):
        tester = app.test_client(self)
        response = tester.get("/hi")
        self.assertTrue(b"Saravanan Vijayamuthu" in response.data)


if __name__ == "__main__":
    unittest.main()

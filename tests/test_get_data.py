import unittest
# from API.services.DBManipulation import fetch_from_db



class MyGetTestCase(unittest.TestCase):
    def test_get_fromdb(self):
        import requests

        url = "https://ubaformapi-jeddubx5l-fastapis-build.vercel.app"
        retreive=requests.get(url,'string')
        # print(retreive.json()["detail"])
        self.assertEqual(isinstance(retreive.json(),dict),True)

if __name__=="__main__":
    unittest.main()        

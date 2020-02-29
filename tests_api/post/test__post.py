from tests_api import functions


class TestDoorwayApiPost:

    def test_проверка_работы_формы_корп_заявки_с_заполненными_полями(self, client):
        res = client.create_corporate()
        functions.check_status(res.status_code)

    def test_проверка_работы_формы_корп_заявки_с_пустыми_полями(self, client):
        res = client.create_corporate_empty()
        res_load = functions.convert_dist(res)

        assert res_load["email"][0] == "Это поле обязательно."
        print("email - Это поле обязательно.")
        assert res_load["phone"][0] == "Это поле обязательно."
        print("phone - Это поле обязательно.")
        assert res_load["comment"][0] == "Это поле обязательно."
        print("comment - Это поле обязательно.")

        assert res.status_code == 400
        try:
            assert res.status_code == 400, "Status code fail"
            print("Status code = 400")
        except:
            assert res.status_code != 400, "Status code = 400"
            print("Status code fail")

    def test_получение_token_авторизации(self, client):
        given = {'username': 'your_username', 'password': 'your_token'}
        res = client.getting_authorization_token(given)
        res_load = functions.convert_dist(res)

        assert res_load[
                   "token"] == "your_token", "token is not equal to your_token"
        print("Token is equal to - your_token. I'ts right.")

        functions.check_status(res.status_code)

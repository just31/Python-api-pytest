from tests_api import functions


class TestDoorwayApiGet:

    def test_запрос_доп_услуг_по_сертификатам(self, client):
        res = client.get_add_certificates()
        res_load = functions.convert_dist(res)

        functions.check_status(res.status_code)

        assert res_load["count"] == 8, "Count result no equal 8"
        print("Count result = 8")
        assert res_load["results"][0]['id'] == 6, "Id first element no equal 6"
        print("Id first element = 6")

    def test_запрос_доп_услуг_по_сертификатам_с_лимитом_и_offset(self, client):
        res = client.get_add_certificates_limit_offset()
        res_load = functions.convert_dist(res)

        assert len(res_load["results"]) == 2, "Array Result len is not 2"
        print("Array Result len is equal 2")

        assert res_load["results"][1]['descr'] == "Описание совпадает"
        print("One of the additional services - Описание совпадает")

        functions.check_status(res.status_code)


    def test_получение_списка_лучших_мероприятий(self, client):
        res = client.get_best_events()
        res_load = functions.convert_dist(res)

        assert len(res_load["result"]) != 0, "Result arr is empty"
        print("Result arr is not empty")
        assert res_load["count"] != 0, "Count value equal 0"
        print("Count value more 0")

        functions.check_status(res.status_code)

    def test_получение_площадки(self, client):
        res = client.get_halls()
        res_load = functions.convert_dist(res)

        assert res_load["results"][0]["seo_title"] == "Тайтл совпадает"
        print("Body matches string - Тайтл совпадает")

        assert len(res_load["results"]) == 1, "Results arr is empty"
        print("Results arr is not empty and is equal to 1.")

        functions.check_status(res.status_code)

    def test_CRUD_главной_страницы_площадки(self, client):
        res = client.get_CRUD_main_pahe_halls()
        res_load = functions.convert_dist(res)

        assert res_load["seo_title"] == "Тайтл совпадает"
        print("Body matches string - Тайтл совпадает")

        assert res_load['id'] == 25, "Id places is not 25"
        print("Id places is equal 25")

        functions.check_status(res.status_code)
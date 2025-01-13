import requests


class HH:
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, ):
        """конструктор класса"""
        self.__url = 'https://api.hh.ru/'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {"per_page": 100, "page": 0, "only_with_salary": True}
        self.employers = [4307, 4219, 5557093, 2180, 208707, 205, 9694561, 5919632, 5667343, 9301808]

    def get_employers(self):
        """загрузка работодателей"""
        employers_info = []
        for employer_id in self.employers:
            temp_url = f"{self.__url}employers/{employer_id}"
            employer_data = requests.get(temp_url).json()
            employers_info.append(employer_data)

        return employers_info

    def load_vacancies(self):
        """загрузка вакансий"""
        vacancy_info = []
        for employer_id in self.employers:
            self._params["employer_id"] = employer_id
            vacancy_url = f"{self.__url}vacancies"
            response = requests.get(vacancy_url, headers=self._headers, params=self._params)
            vacancies = response.json()['items']
            vacancy_info.extend(vacancies)
        return vacancy_info

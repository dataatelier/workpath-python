from .helpers import create_params, list_to_dataframe

import requests
import os


class Client:
    """
    Class that handles the connection to the Workpath api.
    """

    # mandatory headers
    _headers = {'Accept': 'application/json',
                'Content-type': 'application/json'}
    _base_url = 'https://{company}.workpath.com/api/v1'

    def __init__(self, company: str, api_token: str = os.getenv('WORKPATH_API_TOKEN')):
        self._base_url = self._base_url.format(company=company)
        self._headers['Authorization'] = 'Token {api_token}'.format(api_token=api_token)

    def get_goals(self, start_date=None, end_date=None, team_id=None, query=None, page=1, max_results=None,
                  output_format='dict') -> list:
        """
        Gets and returns all goals from the api.

        :param start_date: start_date of the date range filter.
                           Format: YYYY-MM-DD.
                           When omitted all goals with target_date in the future are returned.
                           Note: Required when end_date given.
        :param end_date: end_date of the date range filter.
                         Format: YYYY-MM-DD.
                         When omitted all goals with target_date in the future are returned.
                         Note: Required when start_date given.
        :param team_id: Id of a Workpath team.
                        When set only goals owned by that team will be returned.
        :param query: Query to search against goal title, goal description, all key_result titles,
                      and all key_result descriptions.
        :param page: Number of first page.
                     Default: first possible page
        :param max_results: Limit of results. If None or larger than actual results all goals are returned.
        :param output_format: Return a dictionary or pandas.DataFrame.
                              Possible values: 'dict' or 'json' -> dictionary
                                               'DataFrame', 'pd.DataFrame', or 'pandas.DataFrame' -> pandas.DataFrame
        :return: Returns all goals from the Workpath api in a list or pandas DataFrame.
        """
        endpoint = 'goals'
        url = '{base_url}/{endpoint}'.format(base_url=self._base_url, endpoint=endpoint)
        params = create_params(start_date=start_date, end_date=end_date, team_id=team_id, query=query, page=page)
        goals = []
        total_pages = 1
        # as long as there are goals left and have fewer goals then wanted
        while params.get('page') <= total_pages and (not max_results or len(goals) < max_results):
            # get more goals
            response = self.request_data(url=url, params=params)
            goals = goals + response.get(endpoint)
            total_pages = response.get('pagination').get('total_pages')
            params['page'] = params.get('page') + 1
        # return all goals or max_results goals
        goals_as_dict = goals[:max_results]
        return list_to_dataframe(list_to_transform=goals_as_dict, output_format=output_format)

    def get_goal(self, goal_id: int) -> dict:
        """
        Gets and returns the data of a specific goal.

        :param goal_id: Id of the goal.
        :return: Data of the goal in a dict.
        """
        endpoint = 'goals'
        url = '{base_url}/{endpoint}/{goal_id}'.format(base_url=self._base_url, endpoint=endpoint, goal_id=goal_id)
        response = self.request_data(url=url)
        return response

    def request_data(self, url, params=None) -> dict:
        """
        Requests the data from the Workpath api.

        :param url: Request url.
        :param params: Optional parameters for get request.
        :return: Json result of the request.
        """
        r = requests.get(url, headers=self._headers, params=params)
        r.raise_for_status()
        return r.json()

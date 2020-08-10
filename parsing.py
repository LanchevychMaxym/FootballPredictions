from bs4 import BeautifulSoup as bs
import requests


def parse_web(season='19-20'):
    if season == '19-20':
        page = requests.get('https://football24.ua/ukrayina_uplfirststage_tables_tag50819/')

    if season == '18-19':
        page = requests.get('https://football24.ua/ukrayina_201819_uplsecondstage_tables_tag79389/')

    if season == '17-18':
        page = requests.get('https://football24.ua/ukrayina_201718_uplsecondstage_tables_tag67709/')

    soup = bs(page.text, 'html.parser')
    dict_teams = {}
    if season == '19-20':
        club_table_list = soup.find(class_="standings-table")
        clubs_statistic_list_items = club_table_list.find_all('tr')
        clubs_statistic_list_items = clubs_statistic_list_items[1:]
        for tr in clubs_statistic_list_items:
            name = tr.find('a').get_text()
            list_of_points = tr.find_all(class_="points")
            team_stat = [
                int(list_of_points[0].get_text()),  # games
                int(list_of_points[1].get_text()),  # wins
                int(list_of_points[2].get_text()),  # draws
                int(list_of_points[3].get_text()),  # loses
                int(list_of_points[4].get_text()),  # goal
                int(list_of_points[5].get_text()),  # misses
                int(list_of_points[6].get_text())]  # scores
            dict_teams[name] = team_stat
        return dict_teams

    club_table_list = soup.find_all(class_="standings-table")
    for i in range(2):
        clubs_statistic_list_items = club_table_list[i].find_all('tr')
        clubs_statistic_list_items = clubs_statistic_list_items[1:]

        for tr in clubs_statistic_list_items:
            name = tr.find('a').get_text()
            list_of_points = tr.find_all(class_="points")
            team_stat = [
                int(list_of_points[0].get_text()),  # games
                int(list_of_points[1].get_text()),  # wins
                int(list_of_points[2].get_text()),  # draws
                int(list_of_points[3].get_text()),  # loses
                int(list_of_points[4].get_text()),  # goal
                int(list_of_points[5].get_text()),  # misses
                int(list_of_points[6].get_text())]  # scores
            dict_teams[name] = team_stat

    return dict_teams

from bs4 import BeautifulSoup
import requests, openpyxl

# Tutorial Used: https://www.youtube.com/watch?v=LCVSmkyB4v8&ab_channel=techTFQ

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'NBA Players Stats'
sheet.append(['Player', 'Position', 'Age', 'Team', 'Games Played', 'Games Started', 'Minutes Played Per Game', 'Field Goals Per Game', 'Field Goal Attempts Per Game', 'Field Goal Percentage', '3-Point Field Goals Per Game', '3-Point Field Goal Attempts Per Game', '3-Point Field Goal Percentage', '2-Point Field Goals Per Game', '2-Point Field Goal Attempts Per Game', '2-Point Field Goal Percentage', 'Effective Field Goal Percentage', 'Free Throws Per Game', 'Free Throw Attempts Per Game', 'Free Throw Percentage', 'Offensive Rebounds Per Game', 'Defensive Rebounds Per Game', 'Total Rebounds Per Game', 'Assists Per Game', 'Steals Per Game', 'Blocks Per Game', 'Turnovers Per Game', 'Personal Fouls Per Game', 'Points Per Game'])

try:
    source = requests.get('https://www.basketball-reference.com/leagues/NBA_2023_per_game.html#per_game_stats::pts_per_g')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    
    player_list = soup.find('tbody').find_all('tr', class_="full_table")
    
    for player in player_list:
        stats = player.find_all('td')
        name = stats[0].text
        pos = stats[1].text
        age = stats[2].text
        team = stats[3].text
        games_played = stats[4].text
        games_started = stats[5].text
        mppg = stats[6].text
        fg = stats[7].text
        fg_attempt = stats[8].text
        fg_percentage = stats[9].text
        threep = stats[10].text
        threep_attempt = stats[11].text
        threep_percentage = stats[12].text
        twop = stats[13].text
        twop_attempt = stats[14].text
        twop_percentage = stats[15].text
        eff_fg_percentage = stats[16].text
        ft = stats[17].text
        ft_attempt = stats[18].text
        ft_percentage = stats[19].text
        off_rebounds = stats[20].text
        def_rebounds = stats[21].text
        tot_rebounds = stats[22].text
        ast = stats[23].text
        stl = stats[24].text
        blk = stats[25].text
        tov = stats[26].text
        fouls = stats[27].text
        pts = stats[28].text

        sheet.append([name, pos, age, team, games_played, games_started, mppg, fg, fg_attempt, fg_percentage, threep, threep_attempt, threep_percentage, twop, twop_attempt, twop_percentage, eff_fg_percentage, ft, ft_attempt, ft_percentage, off_rebounds, def_rebounds, tot_rebounds, ast, stl, blk, tov, fouls, pts])
    
except Exception as e:
    print(e)

excel.save('NBA_Player_Stats.xslx')
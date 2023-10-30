import pandas as pd
import requests
from bs4 import BeautifulSoup



def results(base_url, team_to_find):
    results_list = []
    
    # Round from 1 to 26
    for jornada in range(1, 27):
        url = f"{base_url}{jornada}"
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Search the result for the desired team
        result = None

        matches = soup.find_all('table', class_='uppercase w-100 fs-12_tp fs-11_ml table_resultats')  

        for match in matches:
            
            team1 = match.find('td', {"class": 'p-5 resultats-w-equip tr'}).text.strip()  
            team2 = match.find('td', {"class": 'p-5 resultats-w-equip tl'}).text.strip()  
            score = match.find('td', {"class": 'p-5 resultats-w-resultat tc'}).text.strip().replace("ACTA TANCADA", "")  

            # Verify if team is in the results
            if team_to_find in team1 or team_to_find in team2:
                result = f"{team1} {score} {team2}"
                break  

        if result:
            results_list.append(f"{result}")
        else:
            results_list.append(f"SD ESPANYOL B no se encontró en los resultados de la jornada {jornada}")
    
    return results_list

def clean_results(results_list):
    cleaned_list = [item.replace('\n', '').replace('\t', '') for item in results_list]
    return cleaned_list


def jornada(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    # Find all ROUND and DATES by inspecting the page's HTML structure
    jornadas_and_dates = []

    jornada_elements = soup.find_all('th', {'colspan': '4'})
    date_elements = soup.find_all('th', {'colspan': '3'})

    # Iterate through the elements and collect the information
    for jornada, date in zip(jornada_elements, date_elements):
        jornada_text = jornada.text.strip()
        date_text = date.text.strip()
        jornadas_and_dates.append((jornada_text, date_text))
        
    return jornadas_and_dates


def clean_jornadas (jornadas):
    jornadas_final = [str(item).strip('()') for item in jornadas]
    return jornadas_final


def save_dataframe_to_csv(df, file_path, index=False):
    df.to_csv(file_path, index=index)


def federacion():
    base_url = "https://www.fcf.cat/resultats/2223/futbol-sala/lliga-primera-divisio-catalana-futbol-sala/bcn-gr-2/jornada-"
    team_to_find = "SD ESPANYOL B"
    url = "https://www.fcf.cat/calendari/2223/futbol-sala/lliga-primera-divisio-catalana-futbol-sala/bcn-gr-2"

    results_list = results(base_url, team_to_find)
    results_clean = clean_results(results_list)
    jornadas = jornada (url)
    jornadas_clean = clean_jornadas (jornadas)

    output_dict = {
        "jornada": jornadas_clean,
        "results": results_clean
    }
    df = pd.DataFrame(output_dict) 
    save_dataframe_to_csv(df,'DATA/federacio_sucio.csv', index=False)

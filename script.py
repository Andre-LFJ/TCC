import subprocess
import random
import json

def minifab_invoke_query():
    cmd = './minifab invoke -n fabcar -p \'"queryAllCars"\''
    output = subprocess.check_output(cmd, shell=True)
    return output.decode('utf-8').strip()

def extract_chaincode_results(string):
    start_index = string.find('payload:') + len('payload:')
    end_index = string.find('# STATS')
    if start_index != -1 and end_index != -1:
        results_string = string[start_index:end_index].strip()
        results_list = results_string.split('\n')
        for i in range(len(results_list)):
            result = results_list[i].strip()
            if result.startswith("['") and result.endswith("]',"):
                result = result[2:-3].replace('\\\\"', '"').replace('\\\\', '\\')
                results_list[i] = result
        return '\n'.join(results_list).replace('\\', '')
    return ''

def carro_ruim():
    command = 'minifab invoke -n fabcar -p \'"createCar", "RRR-1111", "BMW", "320i", "black", "Andre", "111", "65", "joinville", "br101", "joinville", "joinville", "leve", "1", "280", "20",  "00:15", "18:00", "11/05/2022"\''
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode('utf-8')

def generate_bad_vehicle_rating():
    # Gerando um número aleatório entre 0 e 1
    rating = random.uniform(0.0, 0.7) 
    # Reduzindo a probabilidade de números maiores que 0.5
    if rating > 0.5:
        rating = random.uniform(0.0, 0.7) 
    # Arredondando o resultado para 2 casas decimais
    rating = round(rating, 2)
    
    return rating


def generate_median_vehicle_rating():
    rating = random.uniform(0.4, 0.8)
    rating = round(rating, 2)
    return rating



def generate_good_vehicle_rating():
    # Gerando um número aleatório entre 0.75 e 1.0
    rating = random.uniform(0.75, 1.0)
    # Reduzindo a probabilidade de valores menores que 0.85
    if rating < 0.85:
        rating = random.uniform(0.75, 1.0)
    # Arredondando o resultado para 2 casas decimais
    rating = round(rating, 2)
    
    return rating



for i in range (10):
    print(generate_good_vehicle_rating())

    

#queryAllCars = (extract_chaincode_results(minifab_invoke_query()))[:-13]

#print(queryAllCars)
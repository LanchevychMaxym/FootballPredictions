from sklearn.linear_model import LinearRegression
import numpy as np
from parsing import *


def read_from_file(file):
    with open(file, encoding="UTF8") as main_file:
        liist = [line.split(',') for line in main_file]
    return liist


def train():
    totalMatchNum = 32 * 12 * 2 + 18 * 12
    numFeatures = 7
    y_Train = np.zeros((totalMatchNum))
    x_Train = np.zeros((totalMatchNum, numFeatures))
    indexCounter = 0
    seasons = ['17-18', '18-19', '19-20']
    for season in seasons:
        teams_vectors = parse_web(season)
        numGamesInYear = teams_vectors['Шахтар'][0] * 12
        xTrainAnnual = np.zeros((numGamesInYear, numFeatures))
        yTrainAnnual = np.zeros((numGamesInYear))
        counter = 0
        if season == '17-18':
            matches = read_from_file("database1718.txt")
        if season == '18-19':
            matches = read_from_file("database1819.txt")
        if season == '19-20':
            matches = read_from_file("database1920.txt")
        for team in teams_vectors.keys():
            for match in matches:
                if match[0] == team:
                    rivals = match[1]
                elif match[1] == team:
                    rivals = match[0]
                else:
                    continue
                t_vector = teams_vectors[team]
                r_vector = teams_vectors[rivals]

                diff = [a - b for a, b in zip(t_vector, r_vector)]

                if len(diff) != 0:
                    xTrainAnnual[counter] = diff
                if match[2] == team + '\n':
                    yTrainAnnual[counter] = 1
                else:
                    yTrainAnnual[counter] = 0
                counter += 1
        x_Train[indexCounter:numGamesInYear + indexCounter] = xTrainAnnual
        y_Train[indexCounter:numGamesInYear + indexCounter] = yTrainAnnual
        indexCounter += numGamesInYear
    return x_Train, y_Train


def createGamePrediction(model, xTrain, yTrain, team1_vector, team2_vector):
    model.fit(xTrain, yTrain)
    diff = [[a - b for a, b in zip(team1_vector, team2_vector)]]
    predictions = model.predict(diff)
    return predictions


def predict(team1, team2):
    xTrain, yTrain = train()
    model = LinearRegression()
    teams = parse_web()
    team1_vector = teams[team1]
    team2_vector = teams[team2]
    prediction_for_first = float(createGamePrediction(model, xTrain, yTrain, team1_vector, team2_vector))
    prediction_for_second = float(createGamePrediction(model, xTrain, yTrain, team2_vector, team1_vector))
    if prediction_for_first < 0.0:
        prediction_for_first = 0.0
    if prediction_for_second < 0.0:
        prediction_for_second = 0.0
    return round(prediction_for_first, 4), round(prediction_for_second, 4)

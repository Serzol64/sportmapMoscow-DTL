#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json
import torch
import geojson
from geojson import Feature, FeatureCollection, Point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def datasetConnect(sheet):
	if sheet == 'objects': return pd.read_excel('data/db.xlsx', sheet_name='Объекты отдельно')
	elif sheet == 'access': return pd.read_excel('data/db.xlsx', sheet_name='Обозначения доступности')
	else: return pd.read_excel('data/db.xlsx', sheet_name='Со спортзонами и видами спорта')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def welcome():
	#Основной сервис для карты

	objectList = datasetConnect('objects')

	features = objectList.apply( lambda row: Feature(geometry=Point((float(row['Долгота (Longitude)']), float(row['Широта (Latitude)'])))), axis=1).tolist('')
	properties = objectList.drop(['Широта (Latitude)', 'Долгота (Longitude)'], axis=1).to_dict('')

	feature_collection = FeatureCollection(features=features, properties=properties)

	return feature_collection

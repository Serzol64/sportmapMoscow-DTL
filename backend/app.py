#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json
import torch
import geojson
import uuid
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

	objectsDB = datasetConnect('objects')
	currentSession = str(uuid.uuid4())

	features = []
    insert_features = lambda X: features.append(
            geojson.Feature(geometry=geojson.Point((X["Долгота (Longitude)"],
                                                    X["Широта (Latitude)"])),
                            properties=dict(objid=X["Ведомственная Организация"],
                                            address=X["Адрес"]))))
    objectsDB.apply(insert_features, axis=1)
    with open('data/objects-', currentSession ,'.geojson', 'w+', encoding='utf8') as fp:
        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)

    with open('data/objects-', currentSession ,'.geojson') as f:
		return f.read()

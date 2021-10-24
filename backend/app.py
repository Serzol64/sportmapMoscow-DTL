#! /usr/bin/env python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import json
import geojson
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def datasetConnect(sheet):

	if sheet == 'objects': return load_workbook('data/db.xlsx').get_sheet_by_name('Объекты отдельно')
	elif sheet == 'access': return load_workbook('data/db.xlsx').get_sheet_by_name('Обозначения доступности')
	else: return load_workbook('data/db.xlsx').get_sheet_by_name('Со спортзонами и видами спорта')

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
	lat = []
	longitude = []
	geoData = []

	for index, row in enumerate(objectsDB.rows):
		if index == 'I': longitude = list(row[index].row)
	for index, row in enumerate(objectsDB.rows):
		if index == 'H': lat = list(row[index].row)

	for i in range(len(lat)): geoData.append((longitude[i], lat[i]))

	response = geojson.MultiPoint(geoData)

	return response












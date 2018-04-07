# -*- coding: utf-8 -*-

import csv
import json
import re
import sys

cavernas = []

lat_re = re.compile('Lat (?P<deg>\d+)° (?P<min>\d+)\' (?P<sec>\d+)" S')
lng_re = re.compile('Lng (?P<deg>\d+)° (?P<min>\d+)\' (?P<sec>\d+)" W')

with open('cavernas.csv') as f:
	for linha in csv.DictReader(f, delimiter='\t'):
		if linha["Município"] != "Florianópolis":
			continue

		caverna = {}
		caverna["nome"] = linha["Código"] + " " + linha["Nome"]

		lat, lng = linha["Coordenadas"].split(":")
		lat = lat_re.match(lat.strip()).groupdict()
		lng = lng_re.match(lng.strip()).groupdict()

		caverna['position'] = {
			"lat": -1 * round(int(lat["deg"]) + (int(lat["min"]) / 60.0) + (int(lat["sec"]) / (60.0 * 60.0)), 6),
			"lng": -1 * round(int(lng["deg"]) + (int(lng["min"]) / 60.0) + (int(lng["sec"]) / (60.0 * 60.0)), 6)
		}

		cavernas.append(caverna)

with open('cavernas.json', 'w') as j:
	j.write(json.dumps(cavernas, indent=4))


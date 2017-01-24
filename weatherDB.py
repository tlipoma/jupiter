from pymongo import MongoClient
import logging
import datetime
import os

class WeatherDB():
	def __init__(self, logger=None):
		# Initiallize logger
		self.logger = logger or logging.getLogger(__name__)

		# Open mongodb connection
		self.logger.info('Initilizing DB connection')
		try:
			MLAB_URI = os.environ['WEATHER_MLAB_URI']
			self.logger.info('Retrieved mlab URI')
		except:
			self.logger.error('Could not find mongodb uri')
		try:
			client = MongoClient(MLAB_URI)
			self.weather_db = client.get_default_database()['metars']
			self.logger.info('Opened weather db')
		except:
			self.logger.error('Could not open mlab db')

	def save_metar(self, met_dic):
		# Reformat for consistancy
		metar = {}
		try:
			metar['station'] = met_dic['station']
			metar['temperature'] = met_dic['temp']
			metar['dewpoint'] = met_dic['dewpoint']
			metar['windDirection'] = met_dic['wind_dir']
			metar['windSpeed'] = met_dic['wind_speed']
			metar['windGust'] = met_dic['wind_gust']
			metar['pressure'] = met_dic['pressure']
			metar['precipitation'] = met_dic['precipitation']
			metar['category'] = met_dic['category']
			metar['recordedTime'] = met_dic['time']
			if type(metar['recordedTime']) != datetime.datetime:
				raise Exception('metar time is not a datetime object')

		except Exception as error:
			self.logger.error('Could not parse met_dic while saving to db: ')
			self.logger.error(error)
			return None

		# Save to db
		try:
			update_dic = {}
			update_dic['station'] = metar['station']
			update_dic['recordedTime'] = metar['recordedTime']
			self.weather_db.update(update_dic, metar, upsert=True)
		except Exception as error:
			self.logger.error('Could not save station data to DB: ')
			self.logger.error(error)
			return None

		return metar

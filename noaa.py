import requests
from BeautifulSoup import BeautifulStoneSoup as soup
import dateutil.parser

RECENT_METAR_URL = 'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecent=true&stationString=PHNL%20'

# suppress ssl warnings
requests.packages.urllib3.disable_warnings()

def get_station_data(station_id):
	req_url = RECENT_METAR_URL + station_id
	r = requests.get(req_url)
	if r.status_code != 200:
		return None
	weather = {}
	try:
		s = soup(r.content)
		weather['station'] = station_id
		weather['time'] = dateutil.parser.parse(s.observation_time.string)
		weather['temp'] = float(s.temp_c.string)
		weather['dewpoint'] = float(s.dewpoint_c.string)
		weather['wind_dir'] = int(s.wind_dir_degrees.string)
		weather['wind_speed'] = int(s.wind_speed_kt.string)
		weather['latitude'] = float(s.latitude.string)
		weather['longitude'] = float(s.longitude.string)
		wind_gust = s.wind_gust_kt
		if wind_gust:
			wind_gust = int(wind_gust.string)
		else:
			wind_gust = 0
		weather['wind_gust'] = wind_gust
		weather['pressure'] = float(s.altim_in_hg.string)
		precip = s.pcp6hr_in
		if precip:
			precip = float(precip.string)
		else:
			precip = 0.0
		weather['precipitation'] = precip
		weather['category'] = s.flight_category.string
	except:
		return None
	return weather

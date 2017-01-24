import logging
import noaa
import weatherDB

WEATHER_STATION_LIST = ['KBDR','KSNC','KDXR','KGON','KHFD','KMMK','KHVN','KOXC','KIJD','KBDL','KGED','KILG','KAAF','KBKV','KCEW','KCTY','KDAB','K54J','KDED','KDTS','KEGC','KFHB','KFLM','KFLL','KFXE','KRSW','KFMY','KFPR','KGNV','KHWO','KIMM','KCRG','KJAX','K42J','KEYW','KX14','KLEE','KMTH','KMKY','KMAI','KMLB','KTMB','KMIA','KOPF','KMBF','KAPF','KRRF','KEVB','KOCF','KOCR','KMCO','KORL','KECP','KPNS','K40J','KPMP','KPGD','K2J9','KSRQ','KX26','KPIE','KSPG','KTLH','KTPA','KTDR','KVRB','KPBI','KGIF','KABY','KACJ','KAMG','KAHN','KATL','KFTY','KPUJ','K6A2','KDNL','KAGS','KBGE','KDZJ','KBIJ','KSSI','K6A1','KCNI','KVPC','KCSG','K9A1','KDQH','KDBN','K27A','KGVL','K3J7','K19A','KMCN','KHQU','KMLJ','KMGR','KMUL','KPDK','KFFC','KRMG','KSAV','KTBR','KSBO','KJYL','KTMA','KTVI','KVLD','KVDI','KIIY','KBED','KBVY','KBOS','KCQX','KMQE','KFIT','KHYA','KLWM','KMVY','KACK','KEWB','KOWD','KORE','KPSF','KPYM','KPVC','KTAN','KBAF','KORH','KNAK','KBWI','KDMH','KCGE','KDMW','KW32','KCGS','KESN','KFME','KFDK','K2G4','KGAI','KHGR','KOXB','KRJD','KSBY','K2W6','KAUG','KBGR','KBHB','KCAR','KB21','K40B','KFVE','KIZG','KGNR','KHUL','KMLT','KPWM','KPQI','KRKD','KSFM','KWVL','KIWI','KADG','KAMN','KAPN','KARB','KBTL','KACB','KSJX','KBEH','KRQB','KCAD','KCFS','KCVX','KFPK','KSLH','KCIU','KOEB','KP59','KDET','KYIP','KDTW','KONZ','KDRM','KESC','KFNT','KFKS','KFFX','KGLR','KGRR','KGOV','KSAW','KCMX','KMGN','KC04','KJYM','KBIV','KHTL','KOZW','KIMT','KAZO','KDUH','KLAN','KD95','KLDM','KMCD','KMBL','KISQ','KRMY','KTEW','KMNM','KTTF','KMOP','KP53','KMKG','KERY','KOSC','KRNP','KPLN','KPTK','KP58','KPZQ','KMBS','KHYX','KLWA','KIRS','KHAI','KTVC','KAVL','KMRH','KBUY','KIGX','KCLT','KCTZ','KJQF','KONX','KECG','KEYF','KFAY','KAKH','KGWW','KGSO','KHSE','KHNZ','KHKY','KOAJ','KGEV','KFFA','KLHZ','KLBT','K1A5','KMEB','KEQY','KMRN','KMWK','KEWN','KRDU','KSIF','KRZZ','KRCZ','KRWI','KTTA','KEHO','K5W8','KSUT','KETC','KCPC','KILM','KINT','KBML','KCON','KAFN','KEEN','KLCI','KLEB','KMHT','KDAW','KHIE','KN85','K12N','KACY','K1N7','KCDW','K17N','KN81','KN12','KN07','KLDJ','KN14','K47N','KMIV','KVAY','KEWR','K26N','K3N6','KN40','K39N','KN87','KSMQ','KFWN','KTEB','KTTN','K4N1','KWWD','KALB','KBGM','KBUF','KD38','KN03','KDSV','KDKK','KELM','KCZG','KFRG','KFZY','KGFL','KVGC','K4G6','K1B1','KISP','KJHW','KJRB','KMSS','KMTP','KMGJ','KMSV','KIAG','KOIC','KJFK','KLGA','KNYC','KOLE','KPEO','KPLB','KPTD','KPOU','KROC','KSLK','K5B2','KHWV','KN23','KSYR','KUCA','KART','KELZ','KFOK','KHPN','KSDC','KAKR','KCAK','KHZY','KLUK','KBKL','KCLE','KCMH','KOSU','KDAY','KMGY','KDFI','KDLZ','KFDY','KFBC','KHAO','KLHQ','KI68','KAOH','KLPR','KMFD','KMNN','KMRT','K4I3','KPHD','KVTA','KPOV','KTDZ','KTOL','KAXV','KUSE','KILN','KBJJ','KYNG','KZZV','KABE','KAOO','KAVP','KBFD','KBTP','KFIG','KMQS','KDYL','KDUJ','KERI','KFKL','K29D','KCXY','KJST','KLNS','KLHV','KGKJ','KMDT','KMPO','KPHL','KPNE','KLOM','KAGC','KPIT','KPTW','KUKT','KRDG','KSEG','KN27','KAFJ','KOQN','KIPT','KTHV','KBID','KUUU','KSFZ','KPVD','KWST','KAND','KCHS','KCEU','KCAE','KCUB','KFLO','KGRD','KGSP','KGMU','KGYH','KHXD','KCRE','KOGB','KLQK','KUZA','KROA','KCHO','KCPK','KDAN','KEMV','KLYH','KHEF','KPHF','KORF','KAKQ','KPVG','KPTB','KOFP','KRIC','KRMN','KJFZ','KXSA','KWAL','KHWY','KIAD','KFYJ','KJGG','KDDH','KBTV','KFSO','KCDA','K6B0','KMPV','KEFK','KRUT','KVSF','K1V4','KBKW','KBLF','KW22','KCRW','KCKB','KEKN','KHTS','KMRB','KMGW','KPKB','KI16','K48I','KHLG','KDA']

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_weather_snapshot(station_array):
	# Build DB connection
	db = weatherDB.WeatherDB(logger)

	logger.info('Attempting to save: ' + str(len(station_array)) + ' weather stations...')
	count = 0
	# Go through station list
	for station in station_array:
		count += 1
		logger.info('Saving data for station #' + str(count) + ' of ' + str(len(station_array)) + ' - ' + station)
		weather_data = noaa.get_station_data(station)
		if weather_data:
			db.save_metar(weather_data)
		else:
			logger.info('Could not get data for ' + station)

	logger.info('Done!')

# Get all weather data
save_weather_snapshot(WEATHER_STATION_LIST)

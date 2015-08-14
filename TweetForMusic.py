from twython import TwythonStreamer
import vlc

APP_KEY = 'xxxxx' #supply the appropriate values for these
APP_SECRET = 'xxxxx' 
OAUTH_TOKEN = 'xxxxx'
OAUTH_TOKEN_SECRET = 'xxxxx'

class TweetStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			s = data['text'].encode('utf-8')
			if s[:4] == "Play":
				try:
					try:
						p[0].stop()
						p.pop(0)
					except:
						pass
					p.append(vlc.MediaPlayer("L:\Music\\"+s[5:(s.index('#')-1)]+".mp3")) #enter path to music directory (in place of L:\Music\)
					p[0].play()
				except:
					pass
				print "Playing."
	
	def on_error(self, status_code, data):
		pass

p = []
		
stream = TweetStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='#hashtag') #enter the hashtag to be searched here
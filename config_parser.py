#python3.x configparser
#ConfigParser in 2.x
#configparser in 3.x
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
					  'Compression': 'yes',
					  'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.sever.com'] = {}
topsecret = config['topsecret.sever.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
#finished


#reading from file
config = configparser.ConfigParser()
config.sections()
config.read('example.ini')
config.sections()



	
input('\nenter to exit...\n')

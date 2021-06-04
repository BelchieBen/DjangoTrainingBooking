from django.apps import AppConfig


class UsersConfig(AppConfig):#Loading the premade users app
    name = 'users'

    def ready(self):#importing the user signals
    	import users.signals

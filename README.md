#Timog

##Deploy to heroku:
First, please setup and deploy according to [heroku document](https://devcenter.heroku.com/articles/getting-started-with-django).

...

After deploy, run `heroku run python manage.py syncdb` to sync database for heroku environment. However, if you see some errors about 'auth', please run `heroku run python manage.py migrate auth` to solve this problem.

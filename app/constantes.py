from warnings import warn

DEBUG = False

SQL_INIT = 'app/sql_init/'
POSTS_HASARD = 2
POSTS_PAR_PAGE = 3
POSTS_PAR_PAGE_DISCUSSION = 6
COMMENTS_PAR_PAGE = 2
API_ROUTE = "/api"
RESULTATS_PAR_PAGE = 3

SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)
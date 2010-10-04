# Django settings for django_cms project.
from os.path import abspath, dirname, join
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

gettext = lambda s: s


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Curtis Ekstrom','curtisekstrom@gmail.com'),
    ('',''),
    ('',''),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3mhwsghthl=qg2ih%v(wqdj=q4p-tf%*)egc=x@+e7q$g4^va^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
     
     'django.core.context_processors.auth',
     'django.core.context_processors.i18n',
     'django.core.context_processors.request',
     'django.core.context_processors.media',
     'cms.context_processors.media',
     

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    ### Django CMS ###
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    
)

ROOT_URLCONF = 'base-cms.urls'

TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'templates') 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    
   
###########  Django CMS Konfiguration  ############
   
    ### django-cms apps ###
    'cms',
    'mptt',
    'publisher',
    
    ### django-cms plugins ###
    #'cms.plugins.text',
    #'cms.plugins.picture',		## Plugins need to be enabled and the database then resynced
    #'cms.plugins.link',
    #'cms.plugins.file',
    #'cms.plugins.snippet',
    #'cms.plugins.googlemap',
    
)

CMS_TEMPLATES = (
    
    ('base.html', gettext('default')),
    ('2col.html', gettext('2 Column')),
    ('3col.html', gettext('3 Column')),
)

CMS_TEMPLATE_INHERITANCE = True

#CMS_PLACEHOLDER_CONF = {						##plugins: A list of plugins that can be added to this placeholder.
												##If not supplied all plugins can be selected.
#        'content': {
#                'plugins': ('TextPlugin', 'PicturePlugin'),		##extra_content:  Extra content that plugins in this placeholder receive.	
#                'extra_context': {"theme":"wide"},
#                'name':gettext("Content")					##name:  the name displayed in the admin.  Internationalizar with gettext...
#},
#'right-column': {
#        "plugins": ('TeaserPlugin', 'LinkPlugin'),
#        "extra_context": {"theme":"small"},
#                'name':gettext("Right Column")
#},
#}

#If this is enabled you get 3 new models in Admin:
#Pages global permissions
#User groups - page
#Users - page
#In the edit-view of the pages you can now assign users to pages and grant them
#permissions. In the global permissions you can set the permissions for users globaly.
#
#If a user has the right to create new users he can now do so in the ?Users - page?.
#But he will only see the users he created. The users he created also can only have
#the rights he already has. So if he has only the right to edit a certain page all users
#he created also only can edit this page. Naturally he can even more limit the rights
#of the users he creates.

#CMS_PERMISSION = True

#If set to true gives you a new column ?moderation? in the tree view.
#You can select to moderate pages or hole trees. If a page is under moderation
#you will recieve an email if somebody changes a page and you will be asked
#to approve the changes. Only after you approved the changes they will be updated
#on the live site. If you change a page you moderate yourself you will need to approve
#it anyway. This allows you change a lot of pages for a new version of the site and can
#go live with all the changes on the same time.
#CMS_MODERATOR = True

#This adds 2 new date-time fields in the advanced-settings tab of the page.
#With this option you can limit the time a page is published.
#CMS_SHOW_END_DATE = True
#CMS_SHOW_START_DATE = True

#This adds a new field ?url overwrite? in your in the advanced-settings tab of the page.
#With this field you can overwrite the whole relative url of the page.
#CMS_URL_OVERWRITE = True

#This adds a new field ?menu title? besides the title field. With this field you can overwrite
#the title that is displayed in the menu.  To access the new title from the template, use 
#  {{ page.get_menu_title }}
#CMS_MENU_TITLE_OVERWRITE = True

#This adds a new field ?redirect? to the advanced-settings tab of the page You can enter a url
#and if someone visits this page he gets redirected to this url.
#CMS_REDIRECTS = True

#This adds a new Fieldset ?SEO Fields? in the page admin. You can set there the Page Title,
#Meta Keywords and the Meta Description
#CMS_SEO_FIELDS = True

#If this is enabled the slugs are not nested in the urls.
#So a page with slug ?world? will have an url ?/world? even it is a child of the page ?hello?
#If disabled the page would have an url: ?/hello/world/?
#CMS_FLAT_URLS = True

#Navigation extenders allow you to extend the menu. In Brief: A tuble with a python path to
#a function that returns a list of navigation nodes
CMS_NAVIGATION_EXTENDERS = ('cmsplugin_photologue.menu.get_nodes', 'Photologue app Navigation')
#        ('shop.navigation.get_nodes', 'Shop Categories'),
#        ('gallery.navigation.get_nodes', 'Galleries'),
#)

#Navigation modifiers are functions in other apps that can modify the navigation.
#They can add, remove, reorder navigation nodes.
#CMS_NAVIGATION_MODIFIERS = (
#        ('blog.navigation.add_blog_categories'),
#)

#You can let cms handle the urls of other 3th party apps and attach them to pages.
#For example you have a page named blog and a blog application. You can attach the
#blog urls.py to the blog page. After this every url after blog page will be handled by the
#blog application. The nice thing about this is the cms can be used in the templates of the
#blog application. So you can use placeholders in the templates and they will be filled up
#with plugins that are defined in the blog page. Also the blog menu item will be selected
#if you are on a page that is handled by the blog application.
CMS_APPLICATIONS_URLS = ('cmsplugin_photologue.urls', 'Photologue app')
#('someapp.urls', 'Some application'),
#('sampleapp.urls_en', 'Sample application English URLs'),
#('sampleapp.urls_de', 'Sample application German URLs'),
#)

#Defines if the slugs should be unique over all sites and languages. This setting is changed
#automatically according to other settings. Do not set it in you settings.py if you don?t know what you are doing.
#CMS_UNIQUE_SLUGS = True

#This adds a new field ?softroot? to you advanced-settings tab in the page. If a page is marked as softroot
#the menu will only display the items till the softroot. If you have a huge site you can partition the menu with this.
#CMS_SOFTROOT = True

#By default django-cms hides the menu items that are not translated yet in the current language.
#With this setting set to False they will show up anyway.
CMS_HIDE_UNTRANSLATED = False

#This will redirect the browser to the same page in an other language if the page is not available in the current language.
CMS_LANGUAGE_FALLBACK = False

#Defines how long page content should be cached, including navigation and admin menu.  Default is 60.
#CMS_CONTENT_CACHE_DURATION = 60

#The path from MEDIA_ROOT to the media files located in cms/media/
#CMS_MEDIA_PATH = "cms/"

#The path to the media root of the cms media files.
#CMS_MEDIA_ROOT = "settings.MEDIA_ROOT + "/cms/"

#By default the cms creates a folder in called ?cms_page_media? in your static files folder where all uploaded media files
#are stored. The media files are stored in subfolders numbered with the id of the page.
#CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

LANGUAGES = (
    ('fr', gettext('French')),
    ('de', gettext('German')),
    ('en', gettext('English')),
)



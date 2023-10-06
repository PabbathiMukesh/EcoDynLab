from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import WebApp.views as views
from WebApp import api_handlers

urlpatterns = [
    path('', views.about, name='about'),
    path('map_fixed_size/', views.map_fixed_size, name='map_fixed_size'),
    path('map_from_gee/', views.map_from_gee, name='map_from_gee'),
    path('map_full_screen/', views.map_full_screen, name='map_full_screen'),
    path('chart_from_netcdf/', views.chart_from_netcdf, name='chart_from_netcdf'),
    path('chart_climateserv/', views.chart_climateserv, name='chart_climateserv'),
    path('chart_sqlite/', views.chart_sqlite, name='chart_sqlite'),
    path('about/', views.about, name='about'),
    path('people/', views.people, name='people'),
    path('projects/', views.projects, name='projects'),
    path('products/', views.products, name='products'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_agency/', views.upload_agency, name='upload_agency'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('pictures/', views.picture_gallery, name='pictures'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('contactus/', views.contactus, name='contactus'),
    path('legal/', views.legal, name='legal'),


    path('home/', views.home, name='home'),


    
    
    path('setup/', views.setup, name='setup'),
    path('feedback/', views.feedback, name='feedback'),
    path('updates/', views.updates, name='updates'),
    path('select_aoi/', views.select_aoi, name='select_aoi'),

    path('login/', views.user_login, name='login'),






    #paper urls
    path('papers/', views.paper_index, name='papers'),
    path('paperindex/', views.paper_index, name='paperindex'),
    path('api/list/', views.paper_list_view),
    path('api/create/', views.paper_create_view),
	path('api/<int:paper_id>/', views.paper_detail_view),

    path('map_chart/', views.map_chart, name='map_chart'),
    path('chart_sqlite/stations/', api_handlers.stations, name='stations'),

    path('map_chart/get-station-coords/', api_handlers.stations, name='get-station-coords'),
    path('chart_from_netcdf/get-timeseries-netcdf/', api_handlers.get_timeseries_netcdf, name='get-timeseries-netcdf'),
    path('chart_climateserv/get-timeseries-climateserv/', api_handlers.get_timeseries_climateserv,
         name='get-timeseries-climateserv'),
    path('chart_sqlite/get-timeseries-sqlite/', api_handlers.get_timeseries_sqlite, name='get-timeseries-sqlite'),

    path('map_chart/get-timeseries-sqlite/', api_handlers.get_timeseries_sqlite, name='get-timeseries-sqlite'),
    path('map_from_gee/get-gee-layer/', api_handlers.get_gee_layer, name='get-gee-layer'),
    path('map_from_gee/get-gee-user-layer/', api_handlers.get_gee_user_layer, name='get-gee-user-layer'),
    path('map_chart/get-measurements/', api_handlers.get_measurements, name='get-measurements'),
    path('import-csv/', views.import_csv, name='import_csv'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

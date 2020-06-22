from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import (DatasetServiceSetting, SpatialDatasetServiceSetting,
                                     CustomSetting, PersistentStoreDatabaseSetting,
                                     WebProcessingServiceSetting, PersistentStoreConnectionSetting)


class Servicetest(TethysAppBase):
    """
    Tethys app class for Servicetest.
    """

    name = 'Servicetest'
    index = 'servicetest:home'
    icon = 'servicetest/images/icon.gif'
    package = 'servicetest'
    root_url = 'servicetest'
    color = '#c0392b'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='servicetest',
                controller='servicetest.controllers.home'
            ),
        )

        return url_maps

    def custom_settings(self):
        return (
            CustomSetting(
                name='thredds_path',
                type=CustomSetting.TYPE_STRING,
                description="Local file path to datasets (same as used by Thredds) (e.g. /home/thredds/myDataFolder/)",
                required=True,
                default='/Users/rileyhales/thredds/gldas/',
            ),
            CustomSetting(
                name='thredds_url',
                type=CustomSetting.TYPE_STRING,
                description="URL to the GLDAS folder on the thredds server (e.g. http://[host]/thredds/gldas/)",
                required=True,
                default='https://tethys2.byu.edu/thredds/wms/testAll/gldas/',
            )
        )

    def web_processing_service_settings(self):
        """
        Example wps_services method.
        """
        wps_services = (
            WebProcessingServiceSetting(
                name='primary_52n',
                description='WPS service for app to use',
                required=True,
            ),
        )

        return wps_services

    def persistent_store_settings(self):
        ps_settings = (
            # Connection only, no database
            PersistentStoreConnectionSetting(
                name='primary',
                description='Connection with superuser role needed.',
                required=True
            ),
            # Connection only, no database
            PersistentStoreConnectionSetting(
                name='creator',
                description='Create database role only.',
                required=False
            ),
            # Spatial database
            PersistentStoreDatabaseSetting(
                name='spatial_db',
                description='for storing important spatial stuff',
                required=True,
                initializer='appsettings.model.init_spatial_db',
                spatial=True,
            ),
            # Non-spatial database
            PersistentStoreDatabaseSetting(
                name='temp_db',
                description='for storing temporary stuff',
                required=False,
                initializer='appsettings.model.init_temp_db',
                spatial=False,
            )
        )
        return ps_settings

    def spatial_dataset_service_settings(self):
        return (
            SpatialDatasetServiceSetting(
                name='geoserver',
                description='Geoserver for serving user uploaded shapefiles',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=False,
            ),
        )

    def dataset_service_settings(self):
        """
        Example dataset_service_settings method.
        """
        ds_settings = (
            DatasetServiceSetting(
                name='primary_ckan',
                description='Primary CKAN service for app to use.',
                engine=DatasetServiceSetting.CKAN,
                required=False,
            ),
            DatasetServiceSetting(
                name='hydroshare',
                description='HydroShare service for app to use.',
                engine=DatasetServiceSetting.HYDROSHARE,
                required=False
            )
        )

        return ds_settings

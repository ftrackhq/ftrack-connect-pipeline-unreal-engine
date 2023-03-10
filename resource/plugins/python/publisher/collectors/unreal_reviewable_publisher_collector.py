# :coding: utf-8
# :copyright: Copyright (c) 2014-2023 ftrack

import ftrack_api

from ftrack_connect_pipeline_unreal import plugin


class UnrealSequencePublisherCollectorPlugin(
    plugin.UnrealPublisherCollectorPlugin
):
    '''Unreal sequence publisher collector plugin'''

    plugin_name = 'unreal_reviewable_publisher_collector'

    def run(self, context_data=None, data=None, options=None):
        '''Return the name of file path from plugin *options*'''

        file_path = options.get('media_path')
        if not file_path:
            return [{'media_path': None}]
        return [{'media_path': file_path}]


def register(api_object, **kw):
    if not isinstance(api_object, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return
    plugin = UnrealSequencePublisherCollectorPlugin(api_object)
    plugin.register()

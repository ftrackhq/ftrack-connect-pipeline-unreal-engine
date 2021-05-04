# :coding: utf-8
# :copyright: Copyright (c) 2014-2021 ftrack

from ftrack_connect_pipeline_qt.client.publish import QtPublisherClient
import ftrack_connect_pipeline.constants as constants
import ftrack_connect_pipeline_qt.constants as qt_constants
import ftrack_connect_pipeline_unreal_engine.constants as unreal_constants

class UnrealPublisherClient(QtPublisherClient):
    ui_types = [constants.UI_TYPE, qt_constants.UI_TYPE,
                unreal_constants.UI_TYPE]

    '''Dockable unreal load widget'''
    def __init__(self, event_manager, parent=None):
        super(UnrealPublisherClient, self).__init__(
            event_manager=event_manager, parent=parent
        )
        self.setWindowTitle('Unreal Pipeline Publisher')

    def post_build(self):
        ''' Change window size '''
        super(UnrealPublisherClient, self).post_build()
        self.setWindowTitle('Unreal Pipeline Publisher')
        self.resize(300, 600)
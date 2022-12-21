# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack
import os
import unreal

# FTRACK_PLUGIN_ID = 0x190319
FTRACK_PLUGIN_TYPE = 'ftrackAssetNode'
LOCKED = 'locked'
ASSET_LINK = 'asset_link'
FTRACK_ROOT_PATH = os.path.realpath(
    os.path.join(unreal.SystemLibrary.get_project_saved_directory(), "ftrack")
)
PROJECT_CONTEXT_STORE_FILE_NAME = "project_context.json"
PROJECT_STATE_FILE_NAME = "project_state.json"

from ftrack_connect_pipeline.constants.asset import *

# :coding: utf-8
# :copyright: Copyright (c) 2014-2021 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_unreal_engine.plugin import BaseUnrealPlugin
from ftrack_connect_pipeline_unreal_engine.asset import FtrackAssetTab


class AssetManagerDiscoverUnrealPlugin(
    plugin.AssetManagerDiscoverPlugin, BaseUnrealPlugin
):
    '''
    Class representing a Asset Manager Discover Unreal Plugin
    '''
    ftrack_asset_class = FtrackAssetTab


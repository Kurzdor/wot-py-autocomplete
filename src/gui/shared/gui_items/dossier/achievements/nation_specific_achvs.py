# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/nation_specific_achvs.py
from dossiers2.custom.helpers import getMechanicEngineerRequirements, getVehicleCollectorRequirements, getTankExpertRequirements, getAllCollectorVehicles
from abstract import NationSpecificAchievement
from abstract.mixins import HasVehiclesList
from collector_vehicle import CollectorVehicleConsts
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class MechEngineerAchievement(HasVehiclesList, NationSpecificAchievement):
    itemsCache = dependency.descriptor(IItemsCache)
    _MEDAL_NAME = 'mechanicEngineer'
    _LIST_NAME = 'vehiclesToResearch'

    def __init__(self, nationID, block, dossier, value=None):
        self._vehTypeCompDescrs = self._parseVehiclesDescrsList(NationSpecificAchievement.makeFullName(self._MEDAL_NAME, nationID), nationID, dossier)
        NationSpecificAchievement.__init__(self, self._MEDAL_NAME, nationID, block, dossier, value)
        HasVehiclesList.__init__(self)

    def isActive(self):
        return not self.getVehiclesData()

    def _readLevelUpValue(self, dossier):
        return len(self.getVehiclesData())

    def _getVehiclesDescrsList(self):
        return self._vehTypeCompDescrs

    @classmethod
    def _parseVehiclesDescrsList(cls, name, nationID, dossier):
        return getMechanicEngineerRequirements(set(), cls.itemsCache.items.stats.unlocks, nationID).get(name, []) if dossier is not None and dossier.isCurrentUser() else []


class VehicleCollectorAchievement(HasVehiclesList, NationSpecificAchievement):
    __itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('__hasCollectibleVehicles',)
    _MEDAL_NAME = CollectorVehicleConsts.COLLECTOR_MEDAL_PREFIX
    _NATIONAL_VEHICLES = 'collectorVehiclesByNations'
    _LIST_NAME = 'vehiclesToBuy'

    def __init__(self, nationID, block, dossier, value=None):
        inventoryVehicles = self.__getInventoryCollectibleVehicles(nationID)
        self.__hasCollectibleVehicles = bool(inventoryVehicles)
        self._vehTypeCompDescrs = self._parseVehiclesDescrsList(NationSpecificAchievement.makeFullName(self._MEDAL_NAME, nationID), nationID, dossier, inventoryVehicles)
        NationSpecificAchievement.__init__(self, self._MEDAL_NAME, nationID, block, dossier, value)
        HasVehiclesList.__init__(self)

    def isHidden(self):
        return not (self.__hasCollectibleVehicles or self._isInDossier)

    def isActive(self):
        return not self.getVehiclesData()

    def _readLevelUpValue(self, dossier):
        return len(self.getVehiclesData())

    def _getVehiclesDescrsList(self):
        return self._vehTypeCompDescrs

    @classmethod
    def _getAllSuitableVehicles(cls):
        return getAllCollectorVehicles()

    @classmethod
    def _parseVehiclesDescrsList(cls, name, nationID, dossier, inventoryVehicles=None):
        return getVehicleCollectorRequirements(cls.__getInventoryCollectibleVehicles(nationID) if inventoryVehicles is None else inventoryVehicles, nationID).get(name, []) if dossier is not None and dossier.isCurrentUser() else []

    @classmethod
    def __getInventoryCollectibleVehicles(cls, nationID):
        return set((v for v in getAllCollectorVehicles(nationID) if cls.__itemsCache.items.inventory.getItemData(v) is not None))


class TankExpertAchievement(HasVehiclesList, NationSpecificAchievement):
    _LIST_NAME = 'vehiclesToKill'

    def __init__(self, nationID, block, dossier, value=None):
        self.__vehTypeCompDescrs = self._parseVehiclesDescrsList(NationSpecificAchievement.makeFullName('tankExpert', nationID), dossier)
        NationSpecificAchievement.__init__(self, 'tankExpert', nationID, block, dossier, value)
        HasVehiclesList.__init__(self)
        self.__achieved = dossier is not None and bool(dossier.getRecordValue(*self.getRecordName()))
        return

    def isActive(self):
        return self.__achieved

    def _readLevelUpValue(self, dossier):
        return len(self.getVehiclesData())

    def _getVehiclesDescrsList(self):
        return self.__vehTypeCompDescrs

    @classmethod
    def _parseVehiclesDescrsList(cls, name, dossier):
        return getTankExpertRequirements(dossier.getBlock('vehTypeFrags')).get(name, []) if dossier is not None else []

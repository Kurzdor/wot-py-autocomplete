from gui.veh_post_progression.helpers import getInstalledShells
from gui.veh_post_progression.helpers import setFeatures
from gui.veh_post_progression.helpers import setDisabledSwitches
from gui.veh_post_progression.helpers import updateInvInstalled
from helpers import dependency
from items import vehicles
from battle_modifiers_common import EXT_DATA_MODIFIERS_KEY
from post_progression_common import EXT_DATA_PROGRESSION_KEY
from post_progression_common import EXT_DATA_SLOT_KEY
from post_progression_common import VehicleState
from skeletons.gui.shared.gui_items import IGuiItemsFactory
class VehicleBuilder(object):
    _VehicleBuilder__itemsFactory = dependency.descriptor(IGuiItemsFactory)
    def __init__(self):
        self._VehicleBuilder__invData = None
        self._VehicleBuilder__extData = None
        self._VehicleBuilder__strCD = None

    def setStrCD(self, strCD):
        self._VehicleBuilder__strCD = strCD

    def setCrew(self, crewCDs):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__invData, 'battleCrewCDs')
        self._VehicleBuilder__setInvData('battleCrewCDs', crewCDs)

    def setShells(self, strCD, vehSetups):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__invData, {'shells', 'shellsLayout'})
        vehDescr = vehicles.VehicleDescr(compactDescr = strCD)
        gunDescr = vehDescr.gun
        shellsCDs = vehicles.getDefaultAmmoForGun(gunDescr)[::2]
        shellsLayoutKey = (vehDescr.turret.compactDescr, gunDescr.compactDescr)
        self._VehicleBuilder__updateInvData({'shellsLayout': {shellsLayoutKey: vehSetups['shellsSetups']}, 'shells': getInstalledShells(shellsCDs, vehSetups['shellsSetups'])})

    def setAmmunitionSetups(self, vehSetups, setupIndexes):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__invData, {'eqsLayout', 'layoutIndexes', 'devicesLayout', 'boostersLayout'})
        setupData = {'eqsLayout': vehSetups['eqsSetups'], 'layoutIndexes': setupIndexes, 'devicesLayout': vehSetups['devicesSetups'], 'boostersLayout': vehSetups['boostersSetups']}
        updateInvInstalled(setupData, setupIndexes)
        self._VehicleBuilder__updateInvData(setupData)

    def setRoleSlot(self, slotID):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__extData, EXT_DATA_SLOT_KEY)
        self._VehicleBuilder__setExtData(EXT_DATA_SLOT_KEY, slotID)

    def setPostProgressionState(self, vehPostProgression, disabledSwitchGroupIDs):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__extData, EXT_DATA_PROGRESSION_KEY)
        vehState = VehicleState()
        setFeatures(vehState, vehPostProgression)
        setDisabledSwitches(vehState, disabledSwitchGroupIDs)
        self._VehicleBuilder__setExtData(EXT_DATA_PROGRESSION_KEY, vehState)

    def setModifiers(self, modifiers):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__extData, EXT_DATA_MODIFIERS_KEY)
        self._VehicleBuilder__setExtData(EXT_DATA_MODIFIERS_KEY, modifiers)

    def setSettings(self, settings):
        self._VehicleBuilder__assertNotSet(self._VehicleBuilder__invData, 'settings')
        self._VehicleBuilder__setInvData('settings', settings)

    def getResult(self):
        extData = self._VehicleBuilder__extData.copy() if self._VehicleBuilder__extData is not None else None
        vehicle = self._VehicleBuilder__itemsFactory.createVehicle(self._VehicleBuilder__strCD, extData = extData, invData = self._VehicleBuilder__invData)
        if self._VehicleBuilder__extData and EXT_DATA_PROGRESSION_KEY in self._VehicleBuilder__extData:
            vehicle.installPostProgressionItem(self._VehicleBuilder__itemsFactory.createVehPostProgression(vehicle.compactDescr, self._VehicleBuilder__extData[EXT_DATA_PROGRESSION_KEY], vehicle.typeDescr))
        return vehicle

    def __setInvData(self, key, value):
        if self._VehicleBuilder__invData is None:
            self._VehicleBuilder__invData = {}
        self._VehicleBuilder__invData[key] = value

    def __setExtData(self, key, value):
        if self._VehicleBuilder__extData is None:
            self._VehicleBuilder__extData = {}
        self._VehicleBuilder__extData[key] = value

    def __updateInvData(self, source):
        if self._VehicleBuilder__invData is None:
            self._VehicleBuilder__invData = {}
        self._VehicleBuilder__invData.update(source)

    @staticmethod
    def __assertNotSet(target, keys):
        if target is None:
            return
        else:
            if isinstance(keys, set):
                pass
            return


# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBottomPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelMeta(BaseDAAPIComponent):

    def onBuyOrResearchClick(self):
        self._printOverrideError('onBuyOrResearchClick')

    def onCarouselVehicleSelected(self, intCD):
        self._printOverrideError('onCarouselVehicleSelected')

    def onOfferSelected(self, offerID):
        self._printOverrideError('onOfferSelected')

    def showTooltip(self, intCD, itemType):
        self._printOverrideError('showTooltip')

    def updateData(self, useCompactData):
        self._printOverrideError('updateData')

    def onCouponSelected(self, isActive):
        self._printOverrideError('onCouponSelected')

    def as_setBuyDataS(self, data):
        return self.flashObject.as_setBuyData(data) if self._isDAAPIInited() else None

    def as_setSetItemsDataS(self, data):
        return self.flashObject.as_setSetItemsData(data) if self._isDAAPIInited() else None

    def as_setCouponS(self, data):
        return self.flashObject.as_setCoupon(data) if self._isDAAPIInited() else None

    def as_setSetVehiclesDataS(self, data):
        return self.flashObject.as_setSetVehiclesData(data) if self._isDAAPIInited() else None

    def as_setOffersDataS(self, data):
        return self.flashObject.as_setOffersData(data) if self._isDAAPIInited() else None

    def as_setSetTitleTooltipS(self, tooltip):
        return self.flashObject.as_setSetTitleTooltip(tooltip) if self._isDAAPIInited() else None

    def as_updateLeftTimeS(self, formattedTime, hasHoursAndMinutes=False):
        return self.flashObject.as_updateLeftTime(formattedTime, hasHoursAndMinutes) if self._isDAAPIInited() else None

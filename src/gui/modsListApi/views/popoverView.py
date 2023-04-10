from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView

from ..data import g_dataProvider
from ..events import g_eventsManager

class ModsListPopoverViewMeta(AbstractPopOverView):

	def getModsList(self):
		self._printOverrideError('getModsList')

	def invokeMod(self, modificationID):
		self._printOverrideError('invokeMod')

	def as_setModsDataS(self, data):
		# :param data: Represented by ModsListModsVO (AS)
		if self._isDAAPIInited():
			return self.flashObject.as_setModsData(data)

	def as_setStaticDataS(self, data):
		# :param data: Represented by ModsListStaticDataVO (AS)
		if self._isDAAPIInited():
			return self.flashObject.as_setStaticData(data)

class ModsListPopoverView(ModsListPopoverViewMeta):

	def _populate(self):
		super(ModsListPopoverView, self)._populate()
		g_eventsManager.onListUpdated += self.__collectModsData
		self.as_setStaticDataS(g_dataProvider.staticData)

	def _dispose(self):
		g_eventsManager.onListUpdated -= self.__collectModsData
		super(ModsListPopoverView, self)._dispose()

	def __collectModsData(self):
		self.as_setModsDataS(g_dataProvider.modsData)

	def getModsList(self):
		self.__collectModsData()

	def invokeModification(self, modificationID):
		g_eventsManager.invokeModification(modificationID)

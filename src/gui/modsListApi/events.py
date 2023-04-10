
import Event

__all__ = ('g_eventsManager', )

class EventsManager(object):

	def __init__(self):
		self.onButtonBlinking = Event.Event()
		self.onButtonInvalid = Event.Event()
		self.onListUpdated = Event.Event()
		self.invokeModification = Event.Event()
		self.showPopover = Event.Event()

g_eventsManager = EventsManager()

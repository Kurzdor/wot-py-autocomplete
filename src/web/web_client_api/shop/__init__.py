# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/web/web_client_api/shop/__init__.py
from web.web_client_api import w2capi
from web.web_client_api.shop.actions import ActionsWebApiMixin
from web.web_client_api.shop.boosters import BoostersInfoWebApiMixin
from web.web_client_api.shop.renewable_subscription import RenewableSubWebApiMixin
from web.web_client_api.shop.stats import BalanceWebApiMixin
from web.web_client_api.shop.stock import ItemsWebApiMixin
from web.web_client_api.shop.telecom_rentals import TelecomRentalsWebApiMixin
from web.web_client_api.shop.trade import TradeWebApiMixin
from web.web_client_api.shop.unified_trade_in import UnifiedTradeInWebApiMixin

@w2capi(name='shop', key='action')
class ShopWebApi(ActionsWebApiMixin, BalanceWebApiMixin, ItemsWebApiMixin, TradeWebApiMixin, UnifiedTradeInWebApiMixin, BoostersInfoWebApiMixin, RenewableSubWebApiMixin, TelecomRentalsWebApiMixin):
    pass

from uuid import uuid4
import circle
from circle.apis.tags import crypto_payment_intents_api
from circle.model.create_payment_intent_request import CreatePaymentIntentRequest
from circle.model.crypto_payments_money import CryptoPaymentsMoney
from circle.model.currency import Currency
from circle.model.payment_method_blockchain import PaymentMethodBlockchain
from circle.model.chain import Chain
from circle.apis.tags import balances_api
#from circle.apis.tags import payment_intents_api

# We used the Circle API to create payment intents to transfer funds for bounties on our DAO

# Configure global settings
circle.base_url = circle.Environment.SANDBOX_BASE_URL
circle.api_key = 'SAND_API_KEY:56122a9c31ce77ecb65cd8a842cbdf32:a5ea592c2b4f3975d1bf56233b685c6f'

# Choose API driver
api_instance = balances_api.BalancesApi()

# Send request
try:
    api_response = api_instance.list_balances()
    print(api_response.body)
except circle.ApiException as e:
    print("Exception when calling BalancesApi->list_balances: %s\n" % e)

# Choose API driver
api_instance = crypto_payment_intents_api.CreatePaymentIntent()

# body param
req_body = CreatePaymentIntentRequest(amount=CryptoPaymentsMoney(amount='35.14',
    currency=Currency.USD),
    idempotencyKey=str(uuid4()),
    settlementCurrency=Currency.USD,
    paymentMethods=[PaymentMethodBlockchain(chain=Chain.ETH,type="blockchain")])

try:de
    api_response = api_instance.create_payment_intent(body=req_body)
    print(api_response.body)
except circle.ApiException as ex:
    print("Exception when calling payment_intents_api->create_payment_intent: %s\n" % ex)

payment_intent_id = '7afa2bc8-4a5d-4ee1-862b-08a6edf98bb2'
api_instance = payment_intents_api.PaymentIntentsApi()

# Send request
try:
    api_response = api_instance.get_payment_intent(path_params={'id':payment_intent_id})
    print(api_response)
except circle.ApiException as e:
    print("Exception when calling PaymentIntentsApi->get_payment_intent: %s\n" % e)
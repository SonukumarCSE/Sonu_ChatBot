# from flask import Flask,request,jsonify
# import currencyapicom

# app = Flask(__name__)

# @app.route('/',methods=['POST'])
# def index():
#     data = request.get_json()
#     source_currency = data['queryResult']['parameters']['unit-currency']['currency']
#     amount = data['queryResult']['parameters']['unit-currency']['amount']
#     target_currency = data['queryResult']['parameters']['currency-name']

#     cf = fetch_conversion_factor(source_currency,target_currency)
#     final_amount = amount * cf
#     final_amount = round(final_amount,2)
#     response = {
#         'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
#     }
#     return jsonify(response)


# def fetch_conversion_factor(source,target):

#     client = currencyapicom.Client('cur_live_pXCdSwrTZxSdPeisg1lJXuQnDaLQm0B2qQkSR5ZK')
#     result = client.latest('INR', currencies=['USD'])

#     usd_value = result['data']['USD']['value']

#     print(usd_value)

    

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, request, jsonify
import currencyapicom

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    final_amount = amount * cf
    final_amount = round(final_amount, 2)
    # print(final_amount)
    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    print(response)
    return jsonify(response)

def fetch_conversion_factor(source, target):
    client = currencyapicom.Client('cur_live_pXCdSwrTZxSdPeisg1lJXuQnDaLQm0B2qQkSR5ZK')
    result = client.latest(source, currencies=[target])

    # Access the conversion rate from the result
    conversion_rate = result['data'][target]['value']

    # print("Conversion rate from {} to {} is: {}".format(source, target, conversion_rate))

    return conversion_rate

if __name__ == "__main__":
    app.run(debug=True)

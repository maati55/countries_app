from flask import Flask, jsonify, request
from healthcheck import HealthCheck
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Countries Services App!"

@app.route('/v1/countries')
def query_example():

    target = request.args.get('target')

    # being a restfull api and needing to look up information based on requests it natural to have a db but, I will add it to a db like PostgreSql - there wasn't enough time

    if target == "source":
        return jsonify(
            [{"name": "United Kingdom", "isoCode": "GB"}, {"name": "Ireland", "isoCode": "IE"}, {"name": "France", "isoCode": "FR"}]
        )
    elif target == "destinations":
        return jsonify(
            [{"name": "Spain", "isoCode": "ES"}, {"name": "Ireland", "isoCode": "IE"}, {"name": "France", "isoCode": "FR"}]
        )
    else:
        return 'API request not valid!'

health = HealthCheck(app, "/healthcheck")

def app_health():
	return True, "Health OK"

health.add_check(app_health)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

from flask import Blueprint, request, jsonify

@app.route('/spending-insight', methods=['GET', 'POST'])
def spending_insight():

    return {
        "method": request.method
    }
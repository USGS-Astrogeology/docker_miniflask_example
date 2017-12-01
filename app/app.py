from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def available_packages():
    pkgs = []
    for dist in __import__('pkg_resources').working_set:
        pkgs.append(dist.project_name.replace('Python', ''))

    return jsonify({'response':pkgs})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="80")



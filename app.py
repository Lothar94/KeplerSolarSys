#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import *
from main import *
import json
import urllib
import codecs

app = Flask(__name__)
readPlanets()
planets = getPlanets()

@app.route("/")
def index():
    args = {
        "nDivisions": 100
    }

    if request.args.get("nDivisions",""):
        args["nDivisions"] = int(request.args.get("nDivisions",""))

    png_output = draw2dTrajectories(args["nDivisions"])
    png_output2 = draw3dTrajectories1(args["nDivisions"])
    png_output3 = draw3dTrajectories2(args["nDivisions"])
    png_output4 = draw3dTrajectories3(args["nDivisions"])

    return render_template("index.html",img2d=urllib.quote(png_output.rstrip('\n')),img3d_1=urllib.quote(png_output2.rstrip('\n')),img3d_2=urllib.quote(png_output3.rstrip('\n')),img3d_3=urllib.quote(png_output4.rstrip('\n')), my_planets = planets, code=escape(codecs.open("app.py", "r", "utf-8").read()))

@app.route("/calculate/")
def calculate():
    return render_template("calculate.html", my_planets = planets)

@app.route('/_sun_distance')
def distance_req():
    i = request.args.get('i', 0, type=float)
    p = request.args.get('p', 0, type=int)
    return jsonify(result=planets[p].sunDistanceTime(i))

@app.route('/_energy')
def energy_req():
    i_e = request.args.get('i_e', 0, type=float)
    p_e = request.args.get('p_e', 0, type=int)
    return jsonify(result=str(planets[p_e].energy(i_e)))

@app.route('/_angular_moment')
def angular_moment_req():
    i = request.args.get('i_m', 0, type=float)
    p = request.args.get('p_m', 0, type=int)
    return jsonify(result=planets[p].module_angular_moment(i))

@app.route('/_angular_moment_vector')
def angular_moment_vec_req():
    i = request.args.get('i_mv', 0, type=float)
    p = request.args.get('p_mv', 0, type=int)
    result=planets[p].angular_moment(i)
    print result.tolist()
    return jsonify(str(result.tolist()))

@app.route('/_area')
def area_req():
    i_1 = request.args.get('i_a1', 0, type=float)
    i_2 = request.args.get('i_a2', 0, type=float)
    p = request.args.get('p_a', 0, type=int)
    return jsonify(result=planets[p].area(i_1,i_2))

@app.route('/_position2d')
def pos2d_req():
    i = request.args.get('i_p', 0, type=float)
    p = request.args.get('p_p', 0, type=int)
    return jsonify(result=str(planets[p].positionBessel(i)))

@app.route('/_position3d')
def pos3d_req():
    i = request.args.get('i_p3', 0, type=float)
    p = request.args.get('p_p3', 0, type=int)
    result=planets[p].position3D(i)
    return jsonify(str(result.tolist()))

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)

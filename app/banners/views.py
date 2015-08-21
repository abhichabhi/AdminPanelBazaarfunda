from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask import jsonify
from bson.objectid import ObjectId
from pymongo import ASCENDING
from bson import json_util
import json
from app import mongo
from app import app
from app.decorators import mongoJsonify, jsonResponse
import logging
from app.util import getArgAsList
from logging.handlers import RotatingFileHandler

mod = Blueprint('banners', __name__, url_prefix='/banner')

@mod.route('/hello', methods=['GET'])
def hello():
	return "Hello"

@mod.route('/home/', methods=['GET'])
def homeForm():
	home = mongo.home.find_one()
	TopParallax = home["TopParallax"]
	BottomParallax = home["BottomParallax"]
	Sliderbanner = home["Sliderbanner"]
	MediaPublication = home["MediaPublication"]
	return render_template("homepage.html", TopParallax=TopParallax, BottomParallax=BottomParallax, Sliderbanner=Sliderbanner, MediaPublication=MediaPublication)


@mod.route('/home/submit', methods=['GET'])
def homeFormSubmit():
	TopParallax = getArgAsList(request, 'TBanner')[0]
	BottomParallax = getArgAsList(request, 'PBanner')[0]
	Sliderbanner = getArgAsList(request, 'sliderBanner')
	MediaLink = getArgAsList(request, 'MediaLink')[0]
	MediaBanner = getArgAsList(request, 'MediaBanner')[0]
	MediaDict = {"location":MediaBanner, "link":MediaLink}
	home = mongo.home.find_one()
	if TopParallax == "":
		TopParallax = home["TopParallax"]
	if BottomParallax == "":
		BottomParallax = home["BottomParallax"]
	if Sliderbanner == []:
		Sliderbanner = home["Sliderbanner"]
	MediaPublication = home["MediaPublication"]
	if MediaLink != "" and MediaBanner != "":
		MediaPublication.append(MediaDict)

	homeBannerDict = {"_id":home["_id"], "TopParallax":TopParallax, "BottomParallax":BottomParallax,"Sliderbanner":Sliderbanner, "MediaPublication":MediaPublication}
	updateCollection("home", homeBannerDict)
	return "Hello"

def updateCollection(collection, dict):
	print mongo[collection].save(dict)

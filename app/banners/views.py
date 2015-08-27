from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask import jsonify
from bson.objectid import ObjectId
from pymongo import ASCENDING
from bson import json_util
import json
from app import mongo
from app import babel
from app import app
from app.decorators import mongoJsonify, jsonResponse
import logging
from app.util import getArgAsList
from config import LANGUAGES
from flask.ext.babel import gettext
from logging.handlers import RotatingFileHandler

mod = Blueprint('banners', __name__, url_prefix='/banner')

@babel.localeselector
def get_locale():
	try:
		language = getArgAsList(request, 'lang')[0]
	except:
		language = 'hi'
	print request.accept_languages.best_match(LANGUAGES.keys())
	return language

@mod.route('/hello', methods=['GET'])
def hello():
	flash('Invalid login. Please try again.')
	return "Hello1"

@mod.route('/home/', methods=['GET'])
def homeForm():
	home = mongo.home.find_one()
	TopParallax = home["TopParallax"]
	BottomParallax = home["BottomParallax"]
	Sliderbanner = home["Sliderbanner"]
	MediaPublication = home["MediaPublication"]
	title = gettext("Banners of home page")
	return render_template("homepage.html", TopParallax=TopParallax, BottomParallax=BottomParallax, Sliderbanner=Sliderbanner, MediaPublication=MediaPublication, title = title)

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
	return "Listing form submitted successfully"

@mod.route('/listing', methods=['GET'])
def listingForm():
	try:
		category= getArgAsList(request, 'category')[0]
	except:
		category = 'new'
	print category

	listing = mongo.listing.find_one()
	categoryList = [cat for cat in listing]
	categoryList.pop()
	try:
		categoryListing = listing[category]		
	except:
		categoryListing = listing['dummy']

	compareitems = categoryListing['compareitems']
	hotbrands = categoryListing['hotbrands']
	economicbrands = categoryListing['economicbrands']
	topbanner = categoryListing['topbanner']
	return render_template('listing.html', title="Listing banner : " + category,category=category,categoryList=categoryList, compareitems=compareitems, hotbrands=hotbrands,economicbrands=economicbrands,topbanner=topbanner)

@mod.route('/listing/submit', methods=['GET','PUT'])
def listingFormSubmit():
	if request.method == 'PUT':
		respData =json.loads(request.data)
		category = respData['category']
		data = respData['data']
		print data
		print category
	listing = mongo.listing.find_one()
	listing[category] = data
	updateCollection("listing", listing)
	return "Listing form submitted successfully"

def updateCollection(collection, dict):
	print mongo[collection].save(dict)

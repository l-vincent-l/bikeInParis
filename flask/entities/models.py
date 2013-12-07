#! /usr/bin/python

class Coord(Object):
    def __init__(self, trip_id=None, recorded=None, latitude=None, longitude=None, altitude=None, speed=None, hAccuracy=None, vAccuracy=None):
	self.trip_id;
	self.recorded;
	self.latitude;
	self.longitude;
	self.altitude;
	self.speed;
	self.hAccuracy;
	self.vAccuracy;
}

class Trip(Object):
    def __init__(self, id=None, user_id=None, purpose=None, start=None, stop=None, n_coord=None):
	self.id;
	self.user_id;
	self.purpose;
	self.start;
	self.stop;
	self.n_coord;

class User(Object):
    def __init_(self) 
	self.id;
	self.created;
	self.device;
	self.email;
	self.age;
	self.gender;
	self.homeZIP;
	self.schoolZIP;
	self.workZIP;
	self.cycling_freq;


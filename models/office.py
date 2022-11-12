#!/usr/bin/python3
"""module defines office associated with hospital and doctor"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import requests
# import geocode


class Office(BaseModel, Base):
    """a class office associating doctor and hospital"""
    __tablename__ = "offices"

    geocode_location = Column(Strinf(128), nullable=False)
    country = Column(String(128), nullable = False)
    city = Column(String(128), nullable = False)
    office_address = Column(String(128), nullable = False)
    information = Column(String(128), nullable = False)


    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False) #check with nabil
    hospital_id = Column(String(60), ForeignKey('hospital_affiliation.id'), nullable=False)


    def __init__(self, **kwargs):
        """returns latitude and longitude of office locations on maps"""
        # requests.get(base_url, dictionary of{ APIKEY, address of office}) converted to string using json
        geocode_location = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
            {'API_KEY': 'AIzaSyCZaGxLDW9tX2gnOmqr2TEWo_UxJpVZtzI',
                'address': ''}).json()
        geocode_location.keys()

        # geocode_loaction.keys returns dict of keys['results, 'status]
        if geocode_location['status'] == "OK":
            
            # note the key results contains a dictionary of address components:city/locality/long name/geometry-lat&long
            # since we need the exact location, we use the geometry key which returns a dictionary,
            # containing bounds/location/northeast/southeast etc lat and long
            
            geometry = geocode_location['result'][0]['geometry']
            lat = geometry['location']['lat']
            long = geometry['location']['long']


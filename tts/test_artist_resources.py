import json

from resources.imdb_resources.artist_resource import ArtistResource, ArtistRsp, Artist
from service_factory import ServiceFactory
from resources.base_application_resource import BaseResource, Link




def test_create_and_delete(artist_resource):
    newValues = {"primaryName": "Tom Hanks", "birthYear": 1960}
    result = artist_resource.post(newValues)
    print(result)
    assert False


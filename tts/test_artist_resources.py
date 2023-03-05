import json
import re
from resources.imdb_resources.artist_resource import ArtistResource, ArtistRsp, Artist
from service_factory import ServiceFactory
from resources.base_application_resource import BaseResource, Link


def test_get(artist_resource):
    result = artist_resource.get(primaryName="B.J. Hogg", birthYear='1955')

    assert result[0].data.primaryName == "B.J. Hogg"
    assert result[0].data.birthYear == '1955'
    assert bool(len(result))

def test_create_and_delete(artist_resource):
    newValues = {"primaryName": "Tom Hanks", "birthYear": 1960}
    result = artist_resource.post(newValues)

    assert re.search("nm\d{7}", result) 
    assert artist_resource.update({"primaryName": "Me"},primaryName="Tom Hanks", birthYear="1960")

    assert artist_resource.delete(primaryName="Me", birthYear="1960")


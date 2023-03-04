from unittest.mock import Mock, MagicMock, patch
import pytest


def test_where_clause(mock_svc):
	predicate = {"nameLast": "Williams", "nameFirst": "Ted", "H": 72}
	res, args = mock_svc.predicate_to_where_clause_args(predicate)

	assert res == ' where nameLast=%s and nameFirst=%s and H=%s'
	assert args == ["Williams", "Ted", 72]

def test_set_clause(mock_svc):
	predicate = {"nameLast": "Williams", "nameFirst": "Ted", "H": 72}
	res, args = mock_svc.predicate_to_set_clause_args(predicate)

	assert res == ' set nameLast=%s,nameFirst=%s,H=%s'
	assert args == ["Williams", "Ted", 72]

def test_build_select(mock_svc):
	# Given
	predicate = {"nameLast": "Williams", "nameFirst": "Ted"}

	# When
	sql, args = mock_svc.build_select("lahmansbaseballdb", "people",
								predicate,
								["nameLast", "nameFirst", "birthCity"])
	
	# Then
	assert sql == 'select nameLast,nameFirst,birthCity from lahmansbaseballdb.people where nameLast=%s and nameFirst=%s'
	assert args == ['Williams', 'Ted']


def test_build_delete(mock_svc):
	# Given
	predicate = {"primaryName": "Tom Hanks", "birthYear": 1960}

	# When
	sql, args = mock_svc.build_delete("s23_w4111_hw2_yy3242", "name_basics_all",
								predicate)

	# Then
	assert sql == 'DELETE FROM s23_w4111_hw2_yy3242.name_basics_all where primaryName=%s and birthYear=%s'
	assert args == ['Tom Hanks', 1960]

def test_build_update(mock_svc):

	# Given
	predicate = {"primaryName": "Tom Hanks", "birthYear": 1960}
	newValues = {"Mock": "Me"}

	# When
	sql, args = mock_svc.build_update("s23_w4111_hw2_yy3242", "name_basics_all",
								predicate, newValues)
	
	# Then
	assert sql == 'UPDATE s23_w4111_hw2_yy3242.name_basics_all set Mock=%s where primaryName=%s and birthYear=%s'
	assert args == ['Me', 'Tom Hanks', 1960]


def test_build_create(mock_svc):

	# Given
	newValues = {"primaryName": "Tom Hanks", "birthYear": 1960}

	# When
	sql, args = mock_svc.build_create("s23_w4111_hw2_yy3242", "name_basics_all", newValues)

	# Then
	assert sql == "INSERT INTO s23_w4111_hw2_yy3242.name_basics_all (primaryName,birthYear) VALUES (%s %s )"
	assert args == ["Tom Hanks", 1960]


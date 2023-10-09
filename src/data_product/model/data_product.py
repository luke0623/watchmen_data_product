"""
Data product model
"""

from enum import Enum
from typing import List

from pydantic import BaseModel


class ValueProposition(BaseModel):
	"""
	Value proposition of data product
	"""

	goal: str = None
	why_do_i_need_it: str = None
	what_are_the_benefits: str = None
	who_will_benefit: str = None
	impact_in_business_process: str = None


class DataStatus(Enum):
	"""
	Data status
	"""
	announcement = "announcement"
	draft = "draft"
	development = "development"
	testing = "testing"
	production = "production"
	sunset = "sunset"
	retired = "retired"


class DataProductType(Enum):
	"""
	Data product type
	"""
	API = "API"
	APPLICATION = "APPLICATION"
	DASHBOARD = "DASHBOARD"
	DATASET = "DATASET"
	METRIC = "METRIC"
	OBJECTIVE = "OBJECTIVE"
	REPORT = "REPORT"


class Visibility(Enum):
	"""
	Visibility of data product
	"""
	PRIVATE = "PRIVATE"
	PUBLIC = "PUBLIC"


class UseCase(BaseModel):
	"""
	Use case of data product
	"""
	useCaseTitle: str = None
	useCaseDescription: str = None
	useCaseURL: str = None


class DataHolder(BaseModel):
	"""
	Data holder information
	"""
	businessDomain: str = None


class DataFormat(Enum):
	"""
	Data format
	"""
	CSV = "CSV"
	JSON = "JSON"
	XML = "XML"
	PDF = "PDF"
	EXCEL = "EXCEL"
	WORD = "WORD"
	APPLICATION = "APPLICATION"
	PPT = "PPT"


class DataAuthenticationMethod(Enum):
	"""
	Data authentication method
	"""
	USERNAME_PASSWORD = "USERNAME_PASSWORD"
	API_KEY = "API_KEY"
	OAUTH2 = "OAUTH2"
	OPENID = "OPENID"
	OPENID_CONNECT = "OPENID_CONNECT"
	LDAP = "LDAP"
	NTLM = "NTLM"
	NO_AUTHENTICATION = "NO_AUTHENTICATION"


class DataSpecification(Enum):
	"""
	Data specification
	"""
	Token = "token"
	RAML = "RAML"
	OAS = "OAS"


class DataAccessType(Enum):
	"""
	Data type
	"""

	API = "API"
	URL = "URL"
	FILE = "FILE"


class DataAccess(BaseModel):
	"""
	Data access information
	"""
	dataType: DataAccessType = None
	authenticationMethod: DataAuthenticationMethod = None
	specification: DataSpecification = None
	format: DataFormat = None
	documentationURL: str = None


class DataProduct(BaseModel):
	"""
	Data product information
	"""
	name: str = None
	productID: str = None
	valueProposition: ValueProposition = None
	description: str = None
	visibility: Visibility = Visibility.PRIVATE
	status: str = None
	version: str = None
	categories: List[str] = None
	tags: List[str] = None
	productType: DataProductType = None
	outputFileFormats: List[str] = None
	useCases: List[UseCase] = None


class DataAsset(BaseModel):
	"""
	Data asset information
	"""

	product: DataProduct = None
	dataHolder: DataHolder = None
	dataAccess: DataAccess = None

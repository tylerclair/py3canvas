import requests
import re
import urllib.parse
from . import ACCESS_TOKEN
from . import URL_INSTANCE
import logging

# logging.basicConfig(filename='testing.log',
#                     level=logging.DEBUG,
#                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(message)s')
logger = logging.getLogger("py3canvas.BaseCanvasAPI")


class BaseCanvasAPI(object):
    def __init__(self, initsession=True, **kwargs):
        # self.instance_address = instance_address
        # self.access_token = access_token
        logger.debug(
            "Created new CanvasAPI client for instance: {}.".format(
                "self.instance_address"
            )
        )
        if initsession:
            from . import session

            self.session = session
        # self.session.headers.update({'Authorization': 'Bearer {}'.format(self.access_token)})
        logger.debug(
            "Using Authorization Token authentication method. Added token to headers: {}".format(
                "Authorization: Bearer {}".format(ACCESS_TOKEN)
            )
        )

    @staticmethod
    def uri_for(a):
        return URL_INSTANCE + a

    @staticmethod
    def extract_data_from_response(response, data_key=None):
        """Given a response and an optional data_key should return a dictionary of data returned as part of the response."""
        response_json_data = response.json()
        # Seems to be two types of response, a dict with keys and then lists of data or a flat list data with no key.
        if type(response_json_data) == list:
            # Return the data
            return response_json_data
        elif type(response_json_data) == dict:
            if data_key is None:
                return response_json_data
            else:
                return response_json_data[data_key]
        else:
            raise CanvasAPIError(response)

    @staticmethod
    def extract_pagination_links(response):
        """Given a wrapped_response from a Canvas API endpoint,
        extract the pagination links from the response headers"""
        try:
            link_header = response.links
        except KeyError:
            logger.warning(
                "Unable to find the Link header. Unable to continue with pagination."
            )
            return None
        return link_header

    @staticmethod
    def has_pagination_links(response):
        return "Link" in response.headers

    def depaginate(self, response, data_key=None):
        logging.debug("Attempting to depaginate response from {}".format(response.url))
        all_data = []
        this_data = self.extract_data_from_response(response, data_key=data_key)
        if this_data is not None:
            if type(this_data) == list:
                all_data += this_data
            else:
                all_data.append(this_data)

        if self.has_pagination_links(response):
            pagination_links = self.extract_pagination_links(response)
            try:
                while pagination_links["next"]:
                    response = self.session.get(pagination_links["next"]["url"])
                    pagination_links = self.extract_pagination_links(response)
                    this_data = self.extract_data_from_response(
                        response, data_key=data_key
                    )
                    if this_data is not None:
                        if type(this_data) == list:
                            all_data += this_data
                        else:
                            all_data.append(this_data)
            except KeyError:
                pass
        else:
            logging.warn(
                "Response from {} has no pagination links.".format(response.url)
            )
        return all_data

    def generic_request(
        self,
        method,
        uri,
        all_pages=False,
        data_key=None,
        no_data=False,
        do_not_process=False,
        force_urlencode_data=False,
        data=None,
        params=None,
        files=None,
        single_item=False,
    ):
        """Generic Canvas Request Method."""
        if not uri.startswith("http"):
            uri = self.uri_for(uri)

        if force_urlencode_data is True:
            uri += "?" + urllib.parse.urlencode(data)

        assert method in ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]

        if method == "GET":
            response = self.session.get(uri, params=params)
        elif method == "POST":
            response = self.session.post(uri, data=data, files=files)
        elif method == "PUT":
            response = self.session.put(uri, data=data)
        elif method == "DELETE":
            response = self.session.delete(uri, params=params)
        elif method == "HEAD":
            response = self.session.head(uri, params=params)
        elif method == "OPTIONS":
            response = self.session.options(uri, params=params)

        response.raise_for_status()

        if do_not_process is True:
            return response

        if no_data:
            return response.status_code

        if all_pages:
            return self.depaginate(response, data_key)

        if single_item:
            r = response.json()
            if data_key:
                return r[data_key]
            else:
                return r

        return response.json()

    @staticmethod
    def _validate_enum(value, acceptable_values):
        if not hasattr(value, "__iter__"):
            if value not in acceptable_values:
                raise ValueError("{} not in {}".format(value, str(acceptable_values)))
        else:
            for v in value:
                if v not in acceptable_values:
                    raise ValueError(
                        "{} not in {}".format(value, str(acceptable_values))
                    )
        return value

    @staticmethod
    def _validate_iso8601_string(value):
        """Return the value or raise a ValueError if it is not a string in ISO8601 format."""
        ISO8601_REGEX = (
            r"(\d{4})-(\d{2})-(\d{2})T(\d{2})\:(\d{2})\:(\d{2})([+-](\d{2})\:(\d{2})|Z)"
        )
        if re.match(ISO8601_REGEX, value):
            return value
        else:
            raise ValueError("{} must be in ISO8601 format.".format(value))


class CanvasAPIError(Exception):
    def __init__(self, response):
        self.response = response

    def __unicode__(self):
        return "API Request Failed. Status: {} Content: {}".format(
            self.response.status_code, self.response.content
        )

    def __str__(self):
        return "API Request Failed. Status: {} Content: {}".format(
            self.response.status_code, self.response.content
        )


class BaseModel(object):
    pass


HTTPError = requests.HTTPError

import json

import requests
import xmltodict


class Manager(object):

    def all():
        raise NotImplementedError()

    def get():
        raise NotImplementedError()

    def update():
        raise NotImplementedError()

    def remove():
        raise NotImplementedError()

    def filter():
        raise NotImplementedError()

    def count():
        raise NotImplementedError()


class Driver(object):
    """Base driver for RESTful APIs"""

    def auth():
        """Return tuple with (username, password) authentication"""
        raise NotImplementedError()

    def _create_request(self, url, issue_id, **kwargs):
        # Set the http verb if is specified or GET by default
        http_verb = kwargs['http_verb'] if 'http_verb' in kwargs else 'get'

        # Set user authentication base on the current project and profile
        authentication = kwargs['authentication'] \
            if 'authentication' in kwargs else ()

        # Set the payload for the request if there is data on the kwargs
        data = kwargs['data'] if 'data' in kwargs else {}

        # Create the HTTP request
        r = getattr(requests, http_verb)(url, auth=authentication, params=data)

        if r.status_code == 404:
            # raise IssueDoesNotExist()
            pass

        # Check the response format. TODO: Check by its headers
        if url.endswith('.json'):
            # Parser the JSON text to a python dictionary and return it
            return json.load(r.text)

        elif url.endswith('.xml'):
            # Parse the XML text to a python dictionary and return it
            return xmltodict.parse(r.text)

        # Return the plain text
        return r.text

    class Issue(Manager):
        pass

    class Project(Manager):
        pass

    class TimeTrack(Manager):
        pass


"""
# Since JSON is return an internat error on redmine. Request the xml
url = '{host}/issues/{issue_id}.xml'.format(**{
    'host': self.profile.host,
    'issue_id': issue_id
})


# Load the user authentication from the current role
authentication = (self.profile.username,
                  self.profile.password)
"""

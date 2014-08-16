import requests
import xmltodict

from pmgit.core.base import Base
from pmgit.exceptions import IssueDoesNotExist
from pmgit.messages import CoreMessages, IssueMessages


class Issue(Base):

    def __init__(self, *args, **kwargs):
        super(Issue, self).__init__(*args, **kwargs)

        if len(args) > 0:
            self.redmine = args[0].redmine
            self.profile = args[0].profile
        elif hasattr(self, 'core'):
            self.redmine = self.core.redmine
            self.profile = self.core.profile

    def count(self):
        # Get all the project issues
        issues = self.redmine.issue.filter(project_id=self.current_project.id)

        # Return the number of issues message
        return CoreMessages.number_of_issues(issues.total_count)

    def filter(self, limit=20, **kwargs):
        # Check if there is a description flag on the keyword arguments
        description = 'description' in kwargs and kwargs.pop('description')

        # Check if there is an option checked
        if len(kwargs) == 0:
            # As default set the options to by assigned to the current user
            kwargs['assigned_to_id'] = self.redmine.user.get('current').id

        # Get all the issues with for that options
        issues = self.redmine.issue.filter(sort='status:asc', **kwargs)[:limit]

        # Return all the issues with the issues list format
        return (IssueMessages.issue_format(i, description) for i in issues)

    def all(self, limit=20):
        return self.filter(limit)

    def update(self, *args):
        # self._create_request()
        pass

    def _create_request(self, issue_id, **kwargs):
        # Since JSON is return an internat error on redmine. Request the xml
        url = '{host}/issues/{issue_id}.xml'.format(**{
            'host': self.profile.host,
            'issue_id': issue_id
        })

        # Load the user authentication from the current role
        authentication = (self.profile.username,
                          self.profile.password)

        # Set the http verb if is specified or GET by default
        http_verb = kwargs['http_verb'] if 'http_verb' in kwargs else 'get'

        # Set the payload for the request if there is data on the kwargs
        data = kwargs['data'] if 'data' in kwargs else {}

        # Create the HTTP request
        r = getattr(requests, http_verb)(url, auth=authentication, params=data)

        if r.status_code == 404:
            raise IssueDoesNotExist()

        # Parse the XML text to a python dictonary and return it
        return xmltodict.parse(r.text)['issue']

    def get(self, issue_id):
        return self._create_request(issue_id)

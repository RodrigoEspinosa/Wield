from datetime import datetime

from pmgit.core.base import Base
from pmgit.messages.time_entry import TimeEntryMessages


class TimeEntry(Base):

    def __init__(self, *args, **kwargs):
        super(TimeEntry, self).__init__(*args, **kwargs)

        if hasattr(self, 'core'):
            self.redmine = self.core.redmine

    def all(self):
        # Get the current user
        current_user = self.redmine.user.get('current')

        # Get all the time entries for the current user
        time_entries = self.redmine.time_entry.filter(user_id=current_user.id,
                                                      limit=20)
        # Loop though all the the time entries
        for time_entry in time_entries:
            # Print the issue for each time entry
            print TimeEntryMessages.time_entry_format(time_entry)

    def create(self, **kwargs):
        if 'spent_on' not in kwargs or kwargs['spent_on'] is None:
            # Get the current date in the correct redmine format
            kwargs['spent_on'] = str(datetime.date(datetime.now()))

        return self.redmine.time_entry.create(**kwargs)

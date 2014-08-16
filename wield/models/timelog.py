from os import path, makedirs
from datetime import datetime, timedelta

from pmgit.core.config import ConfigurationFile


class TimeLog(object):
    timelog_dir = None
    datetime_format = '%b %d %Y %I:%M%p'

    def __init__(self):
        # Get the application configuration directory
        conf_dir = ConfigurationFile().conf_directory

        # Set the timelog directory
        self.timelog_dir = path.join(conf_dir, 'timelogs')

        # Check if the directory exists
        if not path.exists(self.timelog_dir):
            # Create the timelog directory
            makedirs(self.timelog_dir)

    def new(self, issue_id):
        # Create the new file
        with self.open(issue_id) as file:
            datetime_ordinal = datetime.now().strftime(self.datetime_format)
            file.write(str(datetime_ordinal) + '\n')

    def open(self, issue_id, openfor='a'):
        try:
            f = open(path.join(self.timelog_dir, issue_id + '.log'), openfor)
            return f

        except IOError:
            # TODO Create this exception
            print 'Log for issue hasn\'t been created'; import sys; sys.exit()

    def get_time(self, issue_id):
        # Initialize the timelog as an empty list
        timelog = []

        # Open as read-only the issue_file
        with self.open(issue_id, 'r') as file:
            # Get each line of the file
            for ln in file:
                # Strip the current line in order to have it clean
                ln_clean = ln.strip()
                # Convert the line to datetime base on the default format
                ln_datetime = datetime.strptime(ln_clean, self.datetime_format)
                # Append the datetime to the timelog list
                timelog.append(ln_datetime)

        # Check if the number of timelogs is odd
        if len(timelog) % 2 != 0:
            # Append the current time to the timelog
            timelog.append(datetime.now().strftime(self.datetime_format))
            # Append the current time to the file in order to have consistency
            self.new(issue_id)

        # Return the timelog list
        return timelog

    def calculate_time(self, issue_id):
        # Get the timelog of the specified issue
        timelog = self.get_time(issue_id)

        # Initialize the timelog sum
        timelog_sum = timedelta()

        # Get each datetime on the timelog
        for i in range(len(timelog)):
            # Check the current entry is even
            if i % 2 == 0:
                # Calculate the time difference between the current
                # timelog and the next one (required to be a pair-list)
                timelog_sum += (timelog[i + 1] - timelog[i])

        # Return the sum of the all timelogs differences
        return timelog_sum

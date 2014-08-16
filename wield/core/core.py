import sys

# Import the required core modules
from pmgit.core.base import Base
from pmgit.core.issue import Issue
from pmgit.core.project import Project
from pmgit.exceptions import IssueDoesNotExist

# Import the required commands
from pmgit.commands.work_on import WorkOn
from pmgit.commands.timelog import TimeLog
from pmgit.commands.work_off import WorkOff
from pmgit.commands.time_entry import TimeEntry

# Import the required messages
from pmgit.messages import IssueMessages, CoreErrors


class Core(Base):

    def register(self):
        # Check if 'issues' is in the command arguments
        if self.args.main == 'issues':
            # Check if there is a number of issues to pull
            number_issues = self.args.id or 20

            # Print a list with all the issues
            for issue in Issue().all(number_issues):
                print issue

        # Check if there id argument is set
        if self.args.id != 0 and self.args.main != 'issues':
            try:
                # Set the current issue
                self.current_issue = Issue().get(self.args.id)

            except IssueDoesNotExist:
                print CoreErrors.does_not_exist('issue')
                sys.exit()

        if self.args.main == 'show':
            # Display the current issue
            IssueMessages.display_issue(self.current_issue)

        elif self.args.main == 'init':
            # Initialzie a new project
            Project.create()

        elif self.args.main == 'workon':
            # Work on the current issue
            WorkOn.issue(self.current_issue)

        elif self.args.main == 'workoff':
            # Workoff the current issue
            WorkOff.issue(self.current_issue)

        elif self.args.main == 'time':
            # Check if the secondary argument is 'toggle' or blank
            if self.args.secondary == 'toggle' or self.args.secondary == '':
                # Run the timelog toggle for the specific issue command
                TimeLog.toggle(self.current_issue)

            # Check if the secondary argument is 'pause'
            elif self.args.secondary == 'pause':
                # Run the timelog pause for the specific issue command
                TimeLog.pause(self.current_issue)

            # Check if the secondary argument is 'resume'
            elif self.args.secondary == 'resume':
                # Run the resume toggle for the specific issue command
                TimeLog.resume(self.current_issue)

        elif self.args.main == 'hours':
            if self.args.secondary == 'all' or self.args.secondary == '':
                TimeEntry.all()
            elif self.args.secondary == 'new':
                TimeEntry.new()

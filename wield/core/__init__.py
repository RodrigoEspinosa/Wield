# Import the Base class at first
from pmgit.core.base import Base

# Import the ConfigurationFile before the rest since is a requirment
from pmgit.core.config import ConfigurationFile

# Import the other modules
from pmgit.core.git import Git
from pmgit.core.core import Core
from pmgit.core.issue import Issue
from pmgit.core.timelog import TimeLog
from pmgit.core.project import Project
from pmgit.core.profile import Profile

# Only for linting. Should never happen.
if __name__ == '__main__':
    Base()
    Git()
    Core()
    Issue()
    TimeLog()
    ConfigurationFile()
    Profile()
    Project()

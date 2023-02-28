import datajoint as dj
from element_animal import subject
from element_animal.subject import Subject
from element_calcium_imaging import imaging, scan
from element_lab import lab
from element_lab.lab import Lab, Location, Project, Protocol, Source, User
from element_session import session_with_datetime as session

from . import db_prefix
from .paths import (
    get_imaging_root_data_dir,
    get_nd2_files,
    get_prairieview_files,
    get_scan_box_files,
    get_scan_image_files,
)
from .reference import Equipment

# ------------- Activate "lab", "subject", "session" schema -------------

lab.activate(db_prefix + "lab")

subject.activate(db_prefix + "subject", linking_module=__name__)

Session = session.Session
Experimenter = lab.User
session.activate(db_prefix + "session", linking_module=__name__)

# ------------- Activate "imaging" schema -------------

imaging.activate(db_prefix + "imaging", db_prefix + "scan", linking_module=__name__)
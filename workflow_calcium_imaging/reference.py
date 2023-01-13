import datajoint as dj

from workflow_calcium_imaging import db_prefix

schema = dj.schema(db_prefix + "reference")


@schema
class Equipment(dj.Lookup):
    definition = """
    scanner: varchar(32)
    """
    contents = zip(["ScannerA"])


@schema
class BrainRegion(dj.Manual):
    definition = """
    acronym: varchar(32)
    ---
    region_name: varchar(128)
    """

import datajoint as dj
import pathlib


def get_imaging_root_data_dir():
    """Retrieve the root data directories containing the imaging data
    for all subjects/sessions (e.g. acquired ScanImage raw files, output files from
    processing routines, etc.).

    Returns:
        Path: Full path to the imaging root data directory, or list of Paths for
        possible root data directories.
    """
    data_dir = dj.config.get("custom", {}).get("imaging_root_data_dir", None)
    return pathlib.Path(data_dir) if data_dir else None


def get_scan_image_files(scan_key):
    """Retrieve the list of ScanImage files associated with a given Scan.

    Args:
        scan_key (dict): Primary key of an entry in Scan table.

    Raises:
        FileNotFoundError: If the session directory associated with the scan_key is not found.
        FileNotFoundError: If no .tif file is found in the session directory associated with the scan_key.

    Returns:
        list: A list of ScanImage files' full file-paths.
    """
    # Folder structure: root / subject / session / .tif (raw)
    data_dir = get_imaging_root_data_dir()

    from .pipeline import session

    sess_dir = data_dir / (session.SessionDirectory & scan_key).fetch1("session_dir")

    if not sess_dir.exists():
        raise FileNotFoundError(f"Session directory not found ({sess_dir})")

    tiff_filepaths = [fp.as_posix() for fp in sess_dir.glob("*.tif")]
    if tiff_filepaths:
        return tiff_filepaths
    else:
        raise FileNotFoundError(f"No tiff file found in {sess_dir}")


def get_scan_box_files(scan_key):
    """Retrieve the list of ScanImage files associated with a given Scan.

    Args:
        scan_key (dict): Primary key of an entry in Scan table.

    Raises:
        FileNotFoundError: If the session directory associated with the scan_key is not found.
        FileNotFoundError: If no .sbx file is found in the session directory associated with the scan_key.

    Returns:
        list: A list of Scanbox files' full file-paths.
    """
    # Folder structure: root / subject / session / .sbx
    data_dir = get_imaging_root_data_dir()

    from .pipeline import session

    sess_dir = data_dir / (session.SessionDirectory & scan_key).fetch1("session_dir")

    if not sess_dir.exists():
        raise FileNotFoundError(f"Session directory not found ({sess_dir})")

    sbx_filepaths = [fp.as_posix() for fp in sess_dir.glob("*.sbx")]
    if sbx_filepaths:
        return sbx_filepaths
    else:
        raise FileNotFoundError(f"No .sbx file found in {sess_dir}")


def get_nd2_files(scan_key):
    """Retrieve the list of Nikon files (*.nd2) associated with a given Scan.

    Args:
        scan_key (dict): Primary key of an entry in Scan table.

    Raises:
        FileNotFoundError: If the session directory associated with the scan_key is not found.
        FileNotFoundError: If no .nd2 file is found in the session directory associated with the scan_key.

    Returns:
        list: A list of Nikon files' full file-paths.
    """
    # Folder structure: root / subject / session / .nd2
    data_dir = get_imaging_root_data_dir()

    from .pipeline import session

    sess_dir = data_dir / (session.SessionDirectory & scan_key).fetch1("session_dir")

    if not sess_dir.exists():
        raise FileNotFoundError(f"Session directory not found ({sess_dir})")

    nd2_filepaths = [fp.as_posix() for fp in sess_dir.glob("*.nd2")]
    if nd2_filepaths:
        return nd2_filepaths
    else:
        raise FileNotFoundError(f"No .nd2 file found in {sess_dir}")


def get_prairieview_files(scan_key):
    """Retrieve the list of Bruker PrairieView tif files (*.tif) with a given Scan.

    Args:
        scan_key (dict): Primary key of an entry in Scan table.

    Raises:
        FileNotFoundError: If the session directory associated with the scan_key is not found.
        FileNotFoundError: If no .tif file is found in the session directory associated with the scan_key.

    Returns:
        list: A list of Bruker PrairieView files' full file-paths.
    """
    # Folder structure: root / subject / session / .tif
    data_dir = get_imaging_root_data_dir()

    from .pipeline import session

    sess_dir = data_dir / (session.SessionDirectory & scan_key).fetch1("session_dir")

    if not sess_dir.exists():
        raise FileNotFoundError(f"Session directory not found ({sess_dir})")

    pv_filepaths = [fp.as_posix() for fp in sess_dir.glob("*.tif")]
    if pv_filepaths:
        return pv_filepaths
    else:
        raise FileNotFoundError(f"No .tif file found in {sess_dir}")

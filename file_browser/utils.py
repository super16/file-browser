from pathlib import Path


def directories_list(path: Path) -> list[Path]:
    """
    List of directories utility function.

    Args:
      path:
        Target Path object.

    Returns:
      List of Path objects which are directories.
    """
    return [x for x in path.iterdir() if x.is_dir()]


def files_list(path: Path) -> list[Path]:
    """
    List of files utility function.

    Args:
      path:
        Target Path object.

    Returns:
      List of Path objects which are files.
    """
    return [x for x in path.iterdir() if x.is_file()]

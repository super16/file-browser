from flask import render_template


def page_not_found(error: FileNotFoundError) -> str:
    """
    404 error function.

    Returns:
      Rendered 404.html.
    """
    return render_template("404.html")


def internal_server_error(error: Exception) -> str:
    """
    500 error function.

    Returns:
      Rendered 500.html.
    """
    return render_template("500.html")


def permission_error(error: PermissionError) -> str:
    """
    Permission error function.
    You're not permitted to read requested directory.

    Returns:
      Rendered permission_error.html.
    """
    return render_template("permission_error.html")

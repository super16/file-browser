from pathlib import Path

from flask import Flask, render_template

from .utils import files_list, directories_list
from .errors import (
    internal_server_error,
    page_not_found,
    permission_error,
)


def create_app() -> Flask:
    """
    Flask file browser app.

    Returns:
      Flask appplication instance.
    """

    app: Flask = Flask(__name__)

    # Views

    @app.route("/<path:subpath>")
    def browse_path_page(subpath: str) -> str:
        """
        Path page function.
        Using browser.html template.

        Returns:
          Rendered template.
        """
        p = Path(f"/{subpath}")
        return render_template(
            "browser.html",
            path=p,
            folder_directory=directories_list(p),
            files_directory=files_list(p),
        )

    @app.route("/")
    def index_page() -> str:
        """
        Index page function.
        Using browser.html template.

        Returns:
          Rendered template.
        """
        p = Path("/")
        return render_template(
            "browser.html",
            path=p,
            folder_directory=directories_list(p),
            files_directory=files_list(p),
        )

    # Errors

    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(FileNotFoundError, page_not_found)
    app.register_error_handler(PermissionError, permission_error)

    return app

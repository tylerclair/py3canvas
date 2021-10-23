"""ImmersiveReader API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI


class ImmersiveReaderAPI(BaseCanvasAPI):
    """ImmersiveReader API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ImmersiveReaderAPI."""
        super(ImmersiveReaderAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ImmersiveReaderAPI")

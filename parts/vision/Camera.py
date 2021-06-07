from abc import ABC, abstractmethod


class Camera(ABC):
    @abstractmethod
    def read_frame(self):
        """Returns an image frame from the currently used camera in OpenCV type."""
        pass
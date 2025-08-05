from abc import ABC, abstractmethod

class FolderManager(ABC):

    @abstractmethod
    def ensure_folder_exists(self, path: str, folder_name: str) -> bool:
        pass

class XmlValidator(ABC):

    @abstractmethod
    def validate(self, file_path: str) -> bool:
        pass

class FileMover(ABC):

    @abstractmethod
    def move_file(self, source_path: str, destination_path: str) -> bool:
        pass

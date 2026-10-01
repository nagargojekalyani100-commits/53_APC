from abc import ABC, abstractmethod


class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Google Drive")

    def download_file(self, filename):
        print(filename, "downloaded from Google Drive")

    def delete_file(self, filename):
        print(filename, "deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Dropbox")

    def download_file(self, filename):
        print(filename, "downloaded from Dropbox")

    def delete_file(self, filename):
        print(filename, "deleted from Dropbox")


class OneDrive(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to OneDrive")

    def download_file(self, filename):
        print(filename, "downloaded from OneDrive")

    def delete_file(self, filename):
        print(filename, "deleted from OneDrive")


# Create objects
google_drive = GoogleDrive()
dropbox = Dropbox()
one_drive = OneDrive()

# Store objects in a list
storage_services = [google_drive, dropbox, one_drive]

# Perform operations
for storage in storage_services:
    storage.upload_file("document.pdf")
    storage.download_file("document.pdf")
    storage.delete_file("document.pdf")
    print()
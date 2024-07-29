import pytest

from twindb_backup.destination.azblob import AzureBlob


@pytest.fixture
def azb():
    return AzureBlob(
        connection_string="DefaultEndpointsProtocol=https;AccountName=aUserAccountName;AccountKey=SuperSecret==;EndpointSuffix=core.usgovcloudapi.net",
        remote_path="azure://computerID.networkstuff.TLD/mysql-fullbackup-file/hourly/mysql/mysql-DATE.xbstream.gz",
        can_do_overwrites=False)

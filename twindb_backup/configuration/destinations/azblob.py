"""Azure Blob Storage destination configuration"""


class AzBlobConfig:  # pylint: disable=too-many-instance-attributes
    """Azure Blob Storage configuration."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        remote_path,
        connection_string,
        can_do_overwrites,
        cpu_cap,
        max_mem_bytes,
        default_protocol,
        default_host_name,
        default_container_name,
        default_interval,
        default_media_type,
        default_fname_prefix,
    ):

        self._remote_path = remote_path
        self._connection_string = connection_string
        self._can_do_overwrites = can_do_overwrites
        self._cpu_cap = cpu_cap
        self._max_mem_bytes = max_mem_bytes
        self._default_protocol = default_protocol
        self._default_host_name = default_host_name
        self._default_container_name = default_container_name
        self._default_interval = default_interval
        self._default_media_type = default_media_type
        self._default_fname_prefix = default_fname_prefix

    @property
    def remote_path(self):
        """Azure URI for where to connect to the backup object[Required]"""
        return self._remote_path

    @property
    def connection_string(self):
        """Azure Connection String[Required]"""
        return self._connection_string

    @property
    def can_do_overwrites(self):
        """Allow overwrites[Optional: Default FALSE]"""
        return self._can_do_overwrites

    @property
    def cpu_cap(self):
        """Constraint for processing restrictions[Optional]"""
        return self._cpu_cap

    @property
    def max_mem_bytes(self):
        """Constraint for processing restrictions[Optional]"""
        return self._max_mem_bytes

    @property
    def default_protocol(self):
        """Protocol for connection to Azure Storage Container[Optional]"""
        return self._default_protocol

    @property
    def default_host_name(self):
        """Hostname for connection to Azure Storage Container[Optional]"""
        return self._default_host_name

    @property
    def default_container_name(self):
        """Azure Storage Container[Optional]"""
        return self._default_container_name

    @property
    def default_interval(self):
        """Backup interval frequency[Optional: Default Yearly]"""
        return self._default_interval

    @property
    def default_media_type(self):
        """Media_type[Optional]"""
        return self._default_media_type

    @property
    def default_fname_prefix(self):
        """Filename prefix[Optional]"""
        return self._default_fname_prefix

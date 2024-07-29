from pathlib import Path

HERE = Path(__file__).parent


def do_set_osenvs(setter_func):
    here = Path(HERE)
    target_dummies = None
    while target_dummies is None and here.name:
        if "dummy_env_vars.json" not in here.iterdir():
            here = here.parent
        else:
            target_dummies = str(here.joinpath("dummy_env_vars.json"))
    setter_func(target_dummies)


PART_NAMES = "store,host,container,interval,media_type,fname".split(",")
SAMPLE_TARGETS = [
    "azure://{host}/mysql-fullbackup-qa1-rms/hourly/mysql/mysql-2020-07-29_01_00_03.xbstream.gz",
    "azure://{host}/mysql-fullbackup-qa1-rms/hourly/mysql/mysql-2020-07-29_01_00_03.xbstream.gz",
]

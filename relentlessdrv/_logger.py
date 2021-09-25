

import logging


def get_logger(logsource, loglevel="WARNING"):

    if loglevel.lower() == "info":
        loglevel = logging.INFO

    elif loglevel.lower() == "debug":
        loglevel = logging.DEBUG

    elif loglevel.lower() == "warning":
        loglevel = logging.WARNING

    elif loglevel.lower() == "error":
        loglevel = logging.ERROR

    elif loglevel.lower() == "critical":
        loglevel = logging.CRITICAL

    else:
        raise ArgumentError(
            "Invalid loglevel argument"
        )

    logfile_pfx = "relentless"
    logfilename = ".".join(logfile_pfx, logsource, "log")

    formatter = logging.Formatter(
        "%(asctime)s --- %(name)s --- %(levelname)s   ||   %(message)s"
    )

    logging.basicConfig(level=loglevel)
    logger = logging.getLogger(logsource)

    ch = logging.StreamHandler()
    #ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(loglevel)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    fh = logging.FileHandler(logfilename)
    fh.setLevel(loglevel)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.propagate = False

    return logger



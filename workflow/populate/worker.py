import datajoint as dj
from datajoint_utilities.dj_worker import DataJointWorker, WorkerLog, ErrorLog

from workflow import db_prefix
from workflow.pipeline import analysis_pop

logger = dj.logger

__all__ = ['standard_worker', 'WorkerLog', 'ErrorLog']


# -------- Define process(s) --------
worker_schema_name = db_prefix + "workerlog"
autoclear_error_patterns = []

# standard process for non-GPU jobs
standard_worker = DataJointWorker('standard_worker',
                                  worker_schema_name,
                                  db_prefix=[db_prefix],
                                  run_duration=1,
                                  sleep_duration=60,
                                  autoclear_error_patterns=autoclear_error_patterns)

# restrict to 1 session
analysis_pop.ROISVDPython.key_source &= {'subject_id': '464724', 'session': 1}

standard_worker(analysis_pop.ROISVDPython)

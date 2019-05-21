# --------------------------------------------------------------------------------
# Programmer: Jason Thorpe
# Date    1/25/2019 3:34:02 PM
# Language:  Python (.py) Version 2.7 or 3.5
# Usage:
#
# Test all model types
#
#     \SpasrseSC > python -m unittest test/test_fit.py
#
# Test a specific model type (e.g. "prospective-restricted"):
#
#     \SpasrseSC > python -m unittest test.test_fit.TestFit.test_retrospective
#
# --------------------------------------------------------------------------------
# pylint: disable=multiple-imports, missing-docstring
"""
usage 

az login

name="rundammit2"
location="westus2"

export BATCH_ACCOUNT_NAME=$name
export BATCH_ACCOUNT_KEY=$(az batch account keys list -n $name -g $name --query primary)
export BATCH_ACCOUNT_URL="https://$name.$location.batch.azure.com"
export STORAGE_ACCOUNT_NAME=$name
export STORAGE_ACCOUNT_KEY=$(az storage account keys list -n $name --query [0].value)

"""


from __future__ import print_function  # for compatibility with python 2.7
import sys, os, random
import unittest
import warnings
from datetime import datetime
from SparseSC.utils.AzureBatch import BatchConfig, run as run_batch_job

try:
    from SparseSC import fit
except ImportError:
    raise RuntimeError("SparseSC is not installed. use 'pip install -e .' to install")


timestamp = datetime.utcnow().strftime("%H%M%S")

class TestFit(unittest.TestCase):

    def test_retrospective(self):

        name = "test43"
        batchdir = os.path.expanduser("~/SparseSC/test/data/batchTest/")


        my_config = BatchConfig(
            POOL_ID= name,
            POOL_LOW_PRIORITY_NODE_COUNT=5,
            POOL_VM_SIZE= "STANDARD_A1_v2",
            JOB_ID= name + timestamp,
            CONTAINER_NAME= name,
            BATCH_DIRECTORY= batchdir,
            DOCKER_CONTAINER = "jdthorpe/sparsesc:latest"
            )

        run_batch_job(my_config)


if __name__ == "__main__":
    # t = TestFit()
    # t.setUp()
    # t.test_retrospective()
    unittest.main()

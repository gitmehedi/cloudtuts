import ssl
import sys

import boto

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

s3_conn = boto.connect_s3()
bucket_name = 's3releaseweb'
bucket = s3_conn.get_bucket(bucket_name)
testfile = "nopaws.html"
key = boto.s3.key.Key(bucket)
key.key = testfile
key.set_contents_from_filename(testfile)

POD_LOGS = '''
{namespace="%s",pod=~".*%s.*"}
'''

APP_LOGS = '''
{namespace="%s",app="%s"}
'''

CONTAINER_LOGS = '''
{namespace="%s",container="%s"}
'''

NAMESPACE_LOGS = '''
{namespace="%s"}
'''

ERRORS = '''
{namespace="%s"} |= "ERROR"
'''

WARNINGS = '''
{namespace="%s"} |= "WARN"
'''

EXCEPTIONS = '''
{namespace="%s"} |= "Exception"
'''

OOM = '''
{namespace="%s"} |= "OOMKilled"
'''

CRASH = '''
{namespace="%s"} |= "CrashLoopBackOff"
'''

IMAGE_PULL = '''
{namespace="%s"} |= "ImagePullBackOff"
'''

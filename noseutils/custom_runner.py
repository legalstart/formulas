import nose

from rm_traceback_plugin import RemoveTraceBackPlugin

if __name__ == '__main__':
    nose.main(addplugins=[RemoveTraceBackPlugin()])

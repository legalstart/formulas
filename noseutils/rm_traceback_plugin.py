import os

from nose.plugins import Plugin


class RemoveTraceBackPlugin(Plugin):

    name = 'removetraceback'

    def options(self, parser, env=os.environ):
        super(RemoveTraceBackPlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        super(RemoveTraceBackPlugin, self).configure(options, conf)
        if not self.enabled:
            return

    def formatFailure(self, test, (exception, msg, traceback)):
        return exception, msg, None

    def formatError(self, test, (exception, msg, traceback)):
        return exception, msg, None

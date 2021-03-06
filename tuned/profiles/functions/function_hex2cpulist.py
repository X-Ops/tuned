import os
import tuned.logs
from . import base
from tuned.utils.commands import commands

log = tuned.logs.get()

class hex2cpulist(base.Function):
	"""
	Conversion function: converts hexadecimal CPU mask to CPU list
	"""
	def __init__(self):
		# one argument
		super(hex2cpulist, self).__init__("hex2cpulist", 1)

	def execute(self, args):
		if not super(hex2cpulist, self).execute(args):
			return None
		return ",".join(str(v) for v in self._cmd.hex2cpulist(args[0]))

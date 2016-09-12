from datetime import datetime
import pytz

from util.terminal_colors import TerminalColors


def debug(message, status=''):
	debugEnabled = True

	if debugEnabled:
		est = pytz.timezone('US/Eastern')
		est_time = datetime.now(est)
		est_time_formatted = est_time.strftime('%r')

		time_str = '[{0}] '.format(est_time_formatted)

		if status == 'warning':
			prefix = TerminalColors.WARNING + 'WARNING' + TerminalColors.ENDC + ': '
		elif status == 'error':
			prefix = TerminalColors.FAIL + 'ERROR  ' + TerminalColors.ENDC + ': '
		elif status == 'test':
			prefix = TerminalColors.OKBLUE + 'TEST   ' + TerminalColors.ENDC + ': '
		else:
			prefix = 'LOG    : '

		print(time_str + prefix + message)